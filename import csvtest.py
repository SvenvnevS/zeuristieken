import csv
import io
import networkx as nx
import matplotlib.pyplot as plt
import random
from networkx.algorithms import bipartite

def main():

	G = nx.Graph()

	# nodes neerzetten per provincie
	with open('nodes.csv', 'r') as csvfile:
		plots = csv.reader(csvfile, delimiter=',')	
		for row in plots:
			G.add_node(str(row[0]),color='None')


	# # lijnen tussen staten
	with open('edges.csv', 'r') as csvfile:
		plots = csv.reader(csvfile, delimiter=',')	
		for row in plots:
			G.add_edge(str(row[0]),str(row[1]))
		
	for node in G.nodes():
		createColor(G, node, controleColor(G, node))

	# red green blue yellow orange purple grey
	score=0
	colormap = []
	print(nx.info(G))
	for node in G.nodes():
		# print(G.nodes[node])
		color=nx.get_node_attributes(G,'color')
		# print(color[node])
		colormap.append(color[node])		
		# nx.draw_networkx(G.nodes[node], with_labels=True,node_color=coloor[node])
	for kleur in colormap:
		if kleur == 'red':
			score += 12
		if kleur == 'green':
			score += 26
		if kleur == 'blue':
			score += 27
		if kleur == 'yellow':
			score += 30
		if kleur == 'orange':
			score += 37
		if kleur == 'purple':
			score += 39
		if kleur == 'grey':
			score += 41
	print("score is: {}".format(score))

	# print(G.nodes())
	print(G. node["Kiev"])
	# print(G["Kiev"])
	nx.draw_networkx(G, with_labels=True,node_color=colormap)

	plt.show()

#gaat een lijst bouwen van toegestane kleuren van de node
def controleColor(G, province):
	kleuren = ""
	colorsAvailable = []
	neighbors = G[province]
	for jemoeder in neighbors:
	 	# print(jemoeder)
	 	print(G.node[jemoeder])
	 	colr=nx.get_node_attributes(G,'color')
	 	kleuren += (colr[jemoeder])
	if 'grey' not in kleuren:
		colorsAvailable.append('grey')
	if 'red' not in kleuren:
		colorsAvailable.append("red")
	if 'green' not in kleuren:
		colorsAvailable.append("green")
	if 'blue' not in kleuren:
		colorsAvailable.append("blue")
	if 'yellow' not in kleuren:
		colorsAvailable.append("yellow")
	if 'orange' not in kleuren:
		colorsAvailable.append("orange")
	if 'purple' not in kleuren:
		colorsAvailable.append("purple")
	return colorsAvailable

#geeft nu random kleuren, maar moet later random.choice uit de lijst van de functio controleColor() geven
def createColor(G, node, colorsAvailable):
	G.nodes[node]['color'] = random.choice(colorsAvailable)

if __name__ == '__main__':
	main()