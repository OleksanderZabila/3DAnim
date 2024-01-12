import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(7, 4))
ax_3d = fig.add_subplot(111, projection='3d')

# Генеруємо дані для графіку
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

# Побудова 3D-графіку
ax_3d.plot_surface(x, y, z, cmap='viridis')

plt.show()
