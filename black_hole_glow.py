import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(facecolor="#161515")
ax.set_facecolor("#040404")
theta = np.linspace(0, 10*np.pi, 2000)
r = 1/(1+0.2*theta)
x, y = r*np.cos(theta), r*np.sin(theta)
ax.scatter(x, y, c=theta, cmap='magma', s=3, edgecolors='none')
ax.scatter([0], [0], color='black', s=180)
ax.axis('equal')
ax.axis('off')
plt.show()