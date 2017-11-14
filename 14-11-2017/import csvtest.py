import csv
import io
import networkx as nx
import matplotlib.pyplot as plt
import random
from networkx.algorithms import bipartite


getalreeks = []

G = nx.Graph()

# nodes neerzetten per provincie
with open('nodes.csv', 'r') as csvfile:
	plots = csv.reader(csvfile, delimiter=',')	
	for row in plots:
		G.add_node(str(row[0]))


# fixed_positions = {str(row[2]):((int(row[3])),(int(row[4])))}

# fixed_nodes = fixed_positions.keys()

# pos = nx.spring_layout(G, pos=fixed_positions, fixed = fixed_nodes)

# # lijnen tussen staten
with open('edges.csv', 'r') as csvfile:
	plots = csv.reader(csvfile, delimiter=',')	
	for row in plots:
		G.add_edge(str(row[0]),str(row[1]))

for x in range(26):
	getal = random.randint(1,7)
	getalreeks.append(getal)
print (getalreeks)


with open(OUTPUT_CSV, 'wb') as output_file:
writer = csv.writer(f)
	



print(nx.info(G))

nx.draw_networkx(G, with_labels=True)

plt.show()