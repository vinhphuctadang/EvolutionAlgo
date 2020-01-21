
import matplotlib.pyplot as plt
import numpy as np

def canvas ():
	return plt

def plot_points (xs, ys):
	return plt.scatter (xs, ys)

def plot_function (f, a=-10,b=10, den=5):
	x = np.linspace (a, b, 20 * (b-a))
	y = [f (_x_) for _x_ in x]
	return plt.plot (x, y)
	
def show ():
	plt.show ()