import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random
import numpy.random as npr
import numpy as np


# Number of steps
n_steps = 100
# Number of random walks
n_walks = 10

walks_x = [[0] * n_steps for i in range(n_walks)]
walks_y = [[0] * n_steps for i in range(n_walks)]
walks_z = [[0] * n_steps for i in range(n_walks)]
walk_x = [0] * n_steps
walk_y = [0] * n_steps
walk_z = [0] * n_steps

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
		# Array of random number
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
		walk_x[j] = x
		walk_y[j] = y
		walk_z[j] = z

	walks_x[i] = [x for x in walk_x]
	walks_y[i] = [y for y in walk_y]
	walks_z[i] = [z for z in walk_z]


mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')


for i in range(0,n_walks):
	ax.plot(walks_x[i], walks_y[i], walks_z[i], label='Random walk')
	ax.scatter(walks_x[i][-1], walks_y[i][-1], walks_z[i][-1], c='b', marker='o') # Ploting final point

# Plot
plt.xlabel('x')
plt.ylabel('y')
#plt.zlabel('z')
ax.legend()
plt.title('Random walks in 3D dimension')
plt.grid(True)
plt.show()
