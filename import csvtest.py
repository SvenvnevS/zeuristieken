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



##	    nodes.append(row['StateCode'])
#	    G.add_node(row['StateCode'])
#	    if row['ColA'] != '':
#	        G.add_edge(row['StateCode'],row['ColA'])
#	    if row['ColC'] != '':
#	        G.add_edge(row['StateCode'],row['ColC'])
#print G.edges()
# B = bipartite.projected_graph(G, nodes)
#print B.edges()