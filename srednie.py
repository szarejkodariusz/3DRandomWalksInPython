import matplotlib.pyplot as plt
import numpy.random as npr
# Definicja funkcji
def calculate(n_walks, n_steps):
	#Lista zawiarajaca pozycje w n-tym kroku
	x2ave = [0.0] * n_steps 
	#Generacja bladzenia losowego
	for i in range(0, n_walks):
		x = 0
		for j in range(0, n_steps):
			rnd = npr.random()
			if rnd < 0.5:
				x = x + 1
			else:
				x = x - 1
			# Poniewaz <x> = 0 warjancje mozemy
			# liczyc w nastepujacy sposob:
			x2ave[j] = x2ave[j] + x**2;
	for i in range(0, n_steps):
		x2ave[i] = float(x2ave[i]) / float(n_walks)
	return x2ave

#Liczba korkow
n_steps = 100
#Liczba drog
n_walks = 100

# Symulacja
x2ave = calculate(n_walks, n_steps)
#Rysowanie
plt.figure()
plt.plot(range(0, n_walks), x2ave, 'o')
plt.plot(range(0, n_walks),range(0, n_walks))
plt.ylabel('<x^2>')
plt.xlabel('step number (=time)')
plt.grid(True)
plt.show()
