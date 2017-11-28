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
		createColor(G, node, controleColor(G, node))


	colormap = []
	for node in G.nodes():
		color=nx.get_node_attributes(G,'color')
		colormap.append(color[node])

	tScore=scoreCounter1(G, colormap)

	print(nx.info(G))

	print("score is: {}".format(tScore))

	nx.draw_networkx(G, with_labels=True,node_color=colormap)

	plt.show()
# end of main


# telt totaal score gebaseerd op kosten tabel 1
def scoreCounter1(G, colormap):
	score = 0
	red = 0
	green = 0
	blue = 0
	yellow = 0
	orange = 0
	purple = 0
	grey = 0

	for kleur in colormap:
		if kleur == 'red':
			red+=1
		if kleur == 'green':
			green+=1
		if kleur == 'blue':
			blue+=1
		if kleur == 'yellow':
			yellow+=1
		if kleur == 'orange':
			orange+=1
		if kleur == 'purple':
			purple+=1
		if kleur == 'grey':
			grey+=1
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
	kleuren = []
	kleuren.append(red)
	kleuren.append(green)
	kleuren.append(blue)
	kleuren.append(yellow)
	kleuren.append(orange)
	kleuren.append(purple)
	kleuren.append(grey)
	print(kleuren)
	bubbleSort(kleuren)
	print(kleuren)
	return score

#gaat een lijst bouwen van toegestane kleuren van de node
def controleColor(G, province):
	kleuren = ""
	colorsAvailable = []
	neighbors = G[province]
	for neighbor in neighbors:
	 	colr=nx.get_node_attributes(G,'color')
	 	kleuren += (colr[neighbor])
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

# copied from http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]<alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

#geeft nu random kleur uit de lijst colorsAvailable
def createColor(G, node, colorsAvailable):
	G.nodes[node]['color'] = random.choice(colorsAvailable)

if __name__ == '__main__':
	main()