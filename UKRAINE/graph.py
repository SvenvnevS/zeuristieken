import networkx as nx
import matplotlib.pyplot as plt
import csv


G = nx.Graph()


G.add_edge(1, 2)
G.add_edge(1, 9)

G.add_edge(2, 9)
G.add_edge(2, 3)
print nx.info(G)

nx.draw(G)

plt.show()

