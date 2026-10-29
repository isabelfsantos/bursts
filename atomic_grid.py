from ase import Atoms
import matplotlib.pyplot as plt

atoms = Atoms("Cu4")

positions = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
atoms.set_positions(positions)
print(atoms)

coordinates = atoms.get_positions()
fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(
    coordinates[:, 0],
    coordinates[:, 1],
    coordinates[:, 2],
    s=500,
    c="darkorange",
    edgecolors="black",
    linewidths=1.5,
)

for index, (x, y, z) in enumerate(coordinates, start=1):
    ax.text(x, y, z, f" Cu {index}", fontsize=10)

ax.set_title("Cu4 Atomic Structure")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_box_aspect((1, 1, 1))
ax.view_init(elev=25, azim=35)
plt.tight_layout()
plt.savefig("atomic_grid.png", dpi=200)
plt.show()