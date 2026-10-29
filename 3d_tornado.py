import pyvista as pv
import numpy as np
x, y, z = np.mgrid[-5:5:30j, -5:5:30j, 0:10:30j]

u = -y
v = x
w = 2 - z/5
grid = pv.StructuredGrid(x, y, z)
grid["vectors"] = np.stack((u, v, w), axis=-1).reshape(-1, 3)
stream = grid.streamlines(vectors="vectors", n_points=200)
plotter = pv.Plotter()
plotter.set_background("black")
plotter.add_mesh(stream, color="purple", line_width=2)
plotter.show()