import networkx as nx
import csv

def dataLoader(file_a, file_b):
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

	
	return G