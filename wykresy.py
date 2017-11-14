import matplotlib.pyplot as plt
import numpy.random as npr

# List containing positio of n-th step
n_walks = 30
n_steps = 100
walks = [[0] * n_steps for i in range(n_walks)]
walk = [0] * n_steps

# Generate random walk
for i in range(0, n_walks):
	x = 0
	for j in range(0, n_steps):
		rnd = npr.random()
		if rnd < 0.5:
			x = x + 1
		else:
			x = x - 1
		walk[j] = x
	walks[i] = [x for x in walk]
plt.figure()

for i in range(0,n_walks):
	plt.plot(walks[i])

# Ploting
plt.ylabel('x')
plt.title('Random walks in one dimension')
plt.xlabel('step number (=time)')
plt.grid(True)
plt.show()

