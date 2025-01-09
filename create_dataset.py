import numpy as np

x = np.linspace(0, 1, 10)
y = np.linspace(0, 1, 10)
X, Y = np.meshgrid(x, y)
Z = 0

for n in range(1, 2, 2):
    Z += (4 / (n*np.pi)) * np.sinh(n*np.pi*X) * np.sin(n*np.pi*Y)

points = np.array([X.flatten(), Y.flatten(), Z.flatten()]).T

np.save('points.npy', points)


