import csv
import StringIO
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite


G = nx.Graph()

# nodes neerzetten per provincie
with open('oekraineprovincies.csv', 'r') as csvfile:
	plots = csv.reader(csvfile, delimiter=',')	
	for row in plots:
		G.add_node(str(row[2]))

# # lijnen tussen staten
with open('oekraineprovincies.csv', 'r') as csvfile:
	plots = csv.reader(csvfile, delimiter=',')	
	for row in plots:
		G.add_edge(str(row[0]),str(row[1]))
	
# fixed_positions = {str(row[2]):((int(row[3])),(int(row[4])))}

# fixed_nodes = fixed_positions.keys()

# pos = nx.spring_layout(G, pos=fixed_positions, fixed = fixed_nodes)



print nx.info(G)

nx.draw_networkx(G, with_labels=True)

plt.show()
