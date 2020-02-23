import matplotlib.pyplot as plt

PAUSE_TIME = 0.5


def hybird(x, y): # 60% of gene will be exchanged to make new individual
	pass	

def populationPlot(X): #2d array of integer
	# plt.clf()
	_x = [x for x in range(9)] * 9
	_y = []
	for _ in range(9):
		_y.extend([_]*9)
	print(_x)
	print(_y)
	# plot.canvas ().pause (0.5)

def main():
	populationPlot(0)
	pass

if __name__=='__main__':
	main()