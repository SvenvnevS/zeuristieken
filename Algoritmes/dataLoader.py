from hill import createColor
from hill import controleColor

import networkx as nx
import csv

def random(file_a, file_b):
	G = nx.Graph()

	# nodes neerzetten per provincie
	with open(file_a, 'r') as csvfile:
		plots = csv.reader(csvfile, delimiter=',')	
		for row in plots:
			G.add_node(str(row[0]),color='None')

	# lijnen tussen staten
	with open(file_b, 'r') as csvfile:
		plots = csv.reader(csvfile, delimiter=',')	
		for row in plots:
			G.add_edge(str(row[0]),str(row[1]))

	# for i in range(5):
	for node in G.nodes():
		# voeg kleur aan een node toe die de buren nog niet hebben
		createColor(G, node, controleColor(G, node))

	return G