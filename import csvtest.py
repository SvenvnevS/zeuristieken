import csv
import io
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite



x = []
y = []


G = nx.Graph()
with open('UKRAINE PROVINCES.csv', 'r') as csvfile:
	plots = csv.reader(csvfile, delimiter=',')	
	for row in plots:
		G.add_edge(str(row[0]),str(row[1]))
		# G.append(str(row[1]))

print(G)

print(nx.info(G))

nx.draw(G, with_labels=True)

plt.show()



	