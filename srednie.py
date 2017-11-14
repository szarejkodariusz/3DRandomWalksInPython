import matplotlib.pyplot as plt
import numpy.random as npr

def calculate(n_walks, n_steps):
	# List containing positio of n-th step
	x2ave = [0.0] * n_steps 
	# Generate random walk
	for i in range(0, n_walks):
		x = 0
		for j in range(0, n_steps):
			rnd = npr.random()
			if rnd < 0.5:
				x = x + 1
			else:
				x = x - 1
			# <x> = 0 so variance can 
			# be calculated in the following way:
			x2ave[j] = x2ave[j] + x**2;
	for i in range(0, n_steps):
		x2ave[i] = float(x2ave[i]) / float(n_walks)
	return x2ave

# Number of steps
n_steps = 100
# Number of pat
n_walks = 100

# Simulate
x2ave = calculate(n_walks, n_steps)
# Ploting
plt.figure()
plt.plot(range(0, n_walks), x2ave, 'o')
plt.plot(range(0, n_walks),range(0, n_walks))
plt.ylabel('<x^2>')
plt.xlabel('step number (=time)')
plt.grid(True)
plt.show()
