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


	# lijnen tussen staten
	with open('edges.csv', 'r') as csvfile:
		plots = csv.reader(csvfile, delimiter=',')	
		for row in plots:
			G.add_edge(str(row[0]),str(row[1]))
		
	for node in G.nodes():
		# voeg kleur aan een node toe die de buren nog niet hebben
		createColor(G, node, controleColor(G, node))


	colormap = []
	for node in G.nodes():

		# vraag de kleur op van een specifieke node
		color = nx.get_node_attributes(G,'color')

		# voeg de kleur toe in de array
		colormap.append(color[node])

	# bereken de score
	tScore = scoreCounter1(G, colormap)

	print(nx.info(G))

	print("score is: {}".format(tScore))

	# teken de map
	# nx.draw_networkx(G, with_labels=True,node_color=colormap)

	plt.show()
# end of main


# telt totaal score gebaseerd op kosten tabel 1
def scoreCounter1(G, colormap):
	score = 0
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
	return score

#gaat een lijst bouwen van toegestane kleuren van de node
def controleColor(G, province):

	kleuren = ""
	colorsAvailable = []

	# vraagt van een node de buren op
	neighbors = G[province]


	for neighbor in neighbors:

		# vraag per provincie de huidige kleur op
	 	colr=nx.get_node_attributes(G,'color')
	 	

	 	# vraag de kleuren op van de buren van een provincie
	 	kleuren += (colr[neighbor])
	 	print(kleuren)

	if 'grey' not in kleuren:
		colorsAvailable.append('grey')
	if 'red' not in kleuren:
		colorsAvailable.append('red')
	if 'green' not in kleuren:
		colorsAvailable.append('green')
	if 'blue' not in kleuren:
		colorsAvailable.append('blue')
	if 'yellow' not in kleuren:
		colorsAvailable.append('yellow')
	if 'orange' not in kleuren:
		colorsAvailable.append('orange')
	if 'purple' not in kleuren:
		colorsAvailable.append('purple')
	return colorsAvailable

# geeft nu random kleur uit de lijst colorsAvailable
def createColor(G, node, colorsAvailable):

	# kleur een node in van een specifieke kleur
	G.nodes[node]['color'] = random.choice(colorsAvailable)

if __name__ == '__main__':
	main()