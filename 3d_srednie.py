import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random
import numpy.random as npr
import numpy as np

def calculate(n_walks, n_steps):
	#Lista zawiarajaca pozycje w n-tym kroku
	x2ave = [0.0] * n_steps
	y2ave = [0.0] * n_steps
	z2ave = [0.0] * n_steps
	r2ave = [0.0] * n_steps
	#Generacja bladzenia losowego
	for i in range(0, n_walks):
		x = 0
		y = 0
		z = 0
		for j in range(0, n_steps):
			# Wektor liczb losowych
			rnd = npr.random(3)-0.5
			# Unormuj
			norm = np.linalg.norm(rnd)
			rnd = rnd / norm
			x = rnd[0] + x
			y = rnd[1] + y
			z = rnd[2] + z
			'''
			# X			
			if npr.random() < 0.5:
				x = rnd[0] + x
				y = rnd[1] + y
				z = rnd[2] + z
			else:
				x = rnd[0] - x
				y = rnd[1] - y
				z = rnd[2] - z
			'''
			
			# Poniewaz <x> = 0 warjancje mozemy
			# liczyc w nastepujacy sposob:
			x2ave[j] = x2ave[j] + x**2;
			y2ave[j] = y2ave[j] + y**2;
			z2ave[j] = z2ave[j] + z**2;
	for i in range(0, n_steps):
		x2ave[i] = float(x2ave[i]) / float(n_walks)
		y2ave[i] = float(y2ave[i]) / float(n_walks)
		z2ave[i] = float(z2ave[i]) / float(n_walks)
		r2ave[i] = x2ave[i] + y2ave[i] + z2ave[i]
	
	return r2ave

#Liczba korkow
n_steps = 100
#Liczba drog
n_walks = 100

# Symulacja
r2ave = calculate(n_walks, n_steps)
#Rysowanie
plt.figure()
plt.plot(range(0, n_walks), r2ave, 'o')
plt.plot(range(0, n_walks),range(0, n_walks))
plt.ylabel('<r^2>')
plt.xlabel('step number (=time)')
plt.title('<r^2> vs time')
plt.grid(True)
plt.show()

'''
mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')

xyz = []
cur = [0, 0, 0]

for _ in xrange(20):
    axis = random.randrange(0, 3)
    cur[axis] += random.choice([-1, 1])
    xyz.append(cur[:])

x, y, z = zip(*xyz)
ax.plot(x, y, z, label='Random walk')
ax.scatter(x[-1], y[-1], z[-1], c='b', marker='o')   # End point
ax.legend()
plt.show()
'''
