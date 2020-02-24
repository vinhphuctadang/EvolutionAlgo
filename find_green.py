import matplotlib.pyplot as plt
import numpy as np
import random as rd
PAUSE_TIME = 0.5

def diffCount(x,y):
	if x < y:
		x,y = y,x
	cnt = 0
	while x:
		cnt += ((x%2) != (y%2))
		x >>=1
		y >>=1
	return cnt
def f(x):
	return diffCount(x, 0b000000001111111100000000)
def environment (x):
	return f(x)
def hybird(x, y): # 50% of gene will be exchanged to make new individual
	# 50*24 bit = 12 bit
	# point mutation
	if rd.randint(0, 9): # 10% point mutation
		bit = rd.randint(0, 23)
		if rd.randint(0, 1):
			# x mutates
			x = x & ~(((x >> bit) % 2) << bit)
		else: 
			# y mutates
			y = y & ~(((y >> bit) % 2) << bit)
	if rd.randint(0, 1):
		return (x & 0b111111111111000000000000) | (y & 0b111111111111)
	return (y & 0b111111111111000000000000) | (x & 0b111111111111)
def getNextGeneration(X, death_rate=0.3):
	result = []
	reshape_X = X.reshape((X.shape[0]*X.shape[1],))
	lst=[]
	for _ in range(len(reshape_X)):
		lst.append((environment(reshape_X[_]), _))
	lst.sort()
	num_death = int(death_rate*len(reshape_X))
	for _, index in lst[0: len(lst)-num_death]:
		result.append(reshape_X[index])
	res_len = len(result)
	# print(lst)
	# print(result)
	for _ in range(num_death):
		_x = result[rd.randint(0, res_len-1)]
		_y = result[rd.randint(0, res_len-1)]
		result.append(hybird(_x, _y))
	return np.array(result).reshape((X.shape[0], X.shape[1]))

def populationPlot(X): #2d array of integer
	plt.clf()
	_x = [x for x in range(X.shape[1])] * X.shape[0]
	_y = []
	for _ in range(X.shape[0]):
		_y.extend([_]*X.shape[1])
	colors = X.reshape(X.shape[0]*X.shape[1])
	print(colors)
	plt.scatter(_x, _y, c=[[((x>>16)&0b11111111)/255, ((x>>8)&0b11111111)/255, (x&0b11111111)/255] for x in colors], s=300)
	plt.pause(0.5)
	plt.show()

def main():
	plt.ion()
	plt.show()
	X = np.array([[rd.randint(0, 255*255*255) for i in range(20)] for j in range(20)], dtype=int) # random population
	generation = 0
	while 1:
		print(f'Generation {generation}')
		populationPlot(X)
		X = getNextGeneration(X, death_rate=0.5)
		generation+=1
	pass

if __name__=='__main__':
	main()
	# print(bitCount(0b10111 & 0b00111))