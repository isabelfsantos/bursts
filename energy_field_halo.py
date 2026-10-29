import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)
X, Y = np.meshgrid(x, y)
tilt = 0.35
radius = np.sqrt(X**2 + (Y / tilt) ** 2)

fig, ax = plt.subplots()
image = ax.imshow(
    np.zeros_like(radius),
    cmap="inferno",
    extent=(-5, 5, -5, 5),
    vmin=-1,
    vmax=1,
    animated=True,
)
ax.axis("off")


def update(frame):
    phase = (frame % 240) / 240
    wave_number = 0.25
    image.set_data(np.sin(wave_number * radius - 2 * np.pi * phase))
    return (image,)


animation = FuncAnimation(fig, update, frames=None, interval=30, blit=True)
plt.show()