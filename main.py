# from now on, X is a set containing x
import plot
import math
import random as rd

# 2 bounds
A = -10
B = 10 
population = 1000

def f (x):
	return (x-9)*(x-3)*(x+4)*(x+2) # edit function here!!!
def environment (x):
	return abs (f(x))

def mutate (x):
	return x + rd.random () * 2 - 1
	
def hybird (x, y):
 	# mutate
 	X = mutate (x)
 	Y = mutate (y)
 	# hybirding
	# actually, it needs to be randomly hybirding (bitwise modification for example), but for simplicity, I just need to calculate their average
 	return (X+Y) / 2

def ageing (X, death_rate=0.4): #randomizingly chose death
	envValues = []
	for i in range(len(X)):
		envValues.append((environment(X[i]), X[i]))
	envValues.sort(reverse=True)
	num_death = int (death_rate * len (X))
	for _ in range (min (num_death, len (X))):
		X.remove(envValues[_][1]) # delete index which contains highest environment value (due to this criteria: as low as possible)	
	print ('%d death' % num_death)
	return X

def thrive (X, birth_rate=0.5): # arbitrarily random 
	
	num_birth = int (birth_rate * len (X))
	tmp = []
	for _ in range (num_birth):
		x = 0
		y = 0
		while x == y:
			x = rd.randrange (0, len (X))
			y = rd.randrange (0, len (X))	
		tmp.append (hybird (X[x], X[y]))

	for x in tmp:
		X.append (x)
	print ('%d proliferated' % num_birth)
	return X
	

def init (num=100, a=-10, b=10):
	X = [(rd.random () * (b-a)+a) for i in range (num)]
	return X

def line (x):
	return 0

def main ():

	# society = init ()
	# # mutation occurs in genes only
	# while 1:
	# 	pass
	plot.canvas ().ion ()
	plot.canvas ().show ()

	X = init (population,a=A,b=B) # random population here!!!
	generation = 0
	try:
		while 1:
			print(f'Generation {generation}')
			plot.canvas ().clf ()
			plot.plot_function (line)
			plot.plot_function (f)
			plot.plot_points (X, [0 for i in X])
			plot.plot_points (X, [f(i) for i in X])
			plot.canvas ().pause (0.5)
			X = thrive (X, birth_rate=0.4) # hybirding performs and returns new generation
			X = ageing (X, death_rate=0.3) 
			generation+=1
			pass
	except Exception as e:
		print (e)
		pass


	pass
if __name__=='__main__':
	main ()	
# plot.canvas ().plot ([1, 2, 3], [1, 4, 9]);
# plot.show ();