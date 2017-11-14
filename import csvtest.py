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
			G.add_node(str(row[2]),color=createColor())


	# # lijnen tussen staten
	with open('oekraineprovincies.csv', 'r') as csvfile:
		plots = csv.reader(csvfile, delimiter=',')	
		for row in plots:
			G.add_edge(str(row[0]),str(row[1]))
		


	# red green blue yellow orange purple grey
	score=0
	colormap = []
	print(nx.info(G))
	for node in G.nodes():
		# print(G.nodes[node])
		color=nx.get_node_attributes(G,'color')
		print(color[node])
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
	nx.draw_networkx(G, with_labels=True,node_color=colormap)

	plt.show()

def createColor():
	i = random.randint(1,7)
	if i is 1:
		return 'red'
	if i is 2:
		return 'green'
	if i is 3:
		return 'blue'
	if i is 4:
		return 'yellow'
	if i is 5:
		return 'orange'
	if i is 6:
		return 'purple'
	if i is 7:
		return 'grey'

if __name__ == '__main__':
	main()