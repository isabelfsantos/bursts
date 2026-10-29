import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

x, y = np.meshgrid(np.linspace(-2, 2, 600), np.linspace(-2, 2, 600))
fig, ax = plt.subplots()
image = ax.imshow(
    np.zeros_like(x),
    cmap="twilight",
    extent=(-2, 2, -2, 2),
    vmin=-1,
    vmax=1,
    animated=True,
)
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis("off")


def update(frame):
    phase = frame * 0.08
    z = np.sin(x**3 - y**3 + phase) * np.cos(x * y + phase)
    image.set_data(z)
    return (image,)


animation = FuncAnimation(fig, update, frames=None, interval=30, blit=True)
plt.show()
