import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random
import numpy.random as npr
import numpy as np

def calculate(n_walks, n_steps):
	# List containing positio of n-th step
	x2ave = [0.0] * n_steps
	y2ave = [0.0] * n_steps
	z2ave = [0.0] * n_steps
	r2ave = [0.0] * n_steps
	# Generate random walk
	for i in range(0, n_walks):
		x = 0
		y = 0
		z = 0
		for j in range(0, n_steps):
			# Array of random numbers
			rnd = npr.random(3)-0.5
			# Norm array
			norm = np.linalg.norm(rnd)
			rnd = rnd / norm
			x = rnd[0] + x
			y = rnd[1] + y
			z = rnd[2] + z
	
			# <x> = 0 so variance can 
			# be calculated in the following way:
			x2ave[j] = x2ave[j] + x**2;
			y2ave[j] = y2ave[j] + y**2;
			z2ave[j] = z2ave[j] + z**2;
	for i in range(0, n_steps):
		x2ave[i] = float(x2ave[i]) / float(n_walks)
		y2ave[i] = float(y2ave[i]) / float(n_walks)
		z2ave[i] = float(z2ave[i]) / float(n_walks)
		r2ave[i] = x2ave[i] + y2ave[i] + z2ave[i]
	
	return r2ave

# Number of steps
n_steps = 100
# Number of random walks
n_walks = 100

# Simulate
r2ave = calculate(n_walks, n_steps)
# Plot
plt.figure()
plt.plot(range(0, n_walks), r2ave, 'o')
plt.plot(range(0, n_walks), range(0, n_walks))
plt.ylabel('<r^2>')
plt.xlabel('step number (=time)')
plt.title('<r^2> vs time')
plt.grid(True)
plt.show()
