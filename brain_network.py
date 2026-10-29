import networkx as nx
import matplotlib.pyplot as plt

G=nx.random_geometric_graph(50,0.3)
plt.figure(figsize=(10,10))
nx.draw(G, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_color='black')
plt.title("Random Geometric Graph")
plt.show()