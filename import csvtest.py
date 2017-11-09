import csv
import StringIO
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite



x = []
y = []


G = nx.Graph()

#lijnen tussen staten
with open('neighborsstates.csv', 'r') as csvfile:
	plots = csv.reader(csvfile, delimiter=',')	
	for row in plots:
		G.add_edge(str(row[0]),str(row[1]))
		
		fixed_positions = (str(row[0]):(int(row[2])),(int(row[3])))

		fixed_nodes = fixed_positions.keys()

		pos = nx.spring_layout(G,pos=fixed_positions, fixed = fixed_nodes)

		nx.draw_networkx(G,pos, with_labels=True)






print nx.info(G)

#nx.draw(G, with_labels=True)

plt.show()