import csv
import StringIO
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite



x = []
y = []


G = nx.Graph()
with open('neighborsstates.csv', 'r') as csvfile:
	plots = csv.reader(csvfile, delimiter=',')	
	for row in plots:
		G.add_edge(str(row[0]),str(row[1]))
		# G.append(str(row[1]))

print(G)

print nx.info(G)

nx.draw(G)

plt.show()



