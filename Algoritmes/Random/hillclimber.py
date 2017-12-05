import csv
import sys
import io
import networkx as nx
import matplotlib.pyplot as plt
import random
import xlwt
import xlrd
from networkx.algorithms import bipartite


def main():

	G = nx.Graph()
	H = nx.Graph()

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

	# lees de oude score uit file
	


		
	for node in G.nodes():
		# voeg kleur aan een node toe die de buren nog niet hebben
		createColor(G, node, controleColor(G, node))


	colormap = []

	# vraag de kleur op van een specifieke node
	color = nx.get_node_attributes(G,'color')
	for node in G.nodes():
		# voeg de kleur toe in de array
		colormap.append(color[node])

	# bereken de score
	tScore1 = scoreCounter1(G, colormap)
	print(tScore1, " score1")
	tScore2 = scoreCounter2(G, colormap)
	print(tScore2, " score2")
	tScore3 = scoreCounter3(G, colormap)
	print(tScore3, " score3")
	tScore4 = scoreCounter4(G, colormap)
	print(tScore4, " score4")

	loopA = 100
	for i in range(loopA):
		if tScore1 < tScore2 and tScore1 < tScore3 and tScore1 < tScore4:
			colormap = hillclimber(G, colormap, 1, tScore1, i , loopA)
			tScore1 = scoreCounter1(G, colormap)
			print(tScore1, " scoreF1")


		if tScore2 < tScore1 and tScore2 < tScore3 and tScore2 < tScore4:
			colormap = hillclimber(G, colormap, 2, tScore2, i , loopA)
			tScore2 = scoreCounter2(G, colormap)
			print(tScore2, " scoreF2")


		if tScore3 < tScore1 and tScore3 < tScore2 and tScore3 < tScore4:
			colormap = hillclimber(G, colormap, 3, tScore3, i , loopA)
			tScore3 = scoreCounter3(G, colormap)
			print(tScore3, " scoreF3")


		if tScore4 < tScore1 and tScore4 < tScore2 and tScore4 < tScore3:
			colormap = hillclimber(G, colormap, 4, tScore4, i , loopA)
			tScore4 = scoreCounter4(G, colormap)
			print(tScore4, " scoreF4")


	nx.draw_networkx(G, with_labels=True,node_color=colormap)
	plt.show()
# end of main

def hillclimber(G, colormap, scorefunctie, maxScore, i , loopA):
	random_nodes = random_node_list(G)
	for node in random_nodes:

		# print(i)
		# if i < ((loopA/4)*3):
		# 	print((loopA-(i+(loopA/4)))/7.5)
		# 	temperature = (loopA-(i+(loopA/4)))/7.5
		# 	if temperature > 20:
		# 		temperature = 20
		# 	print(temperature)
		# 	maxScore = maxScore+temperature
		colorsAv = controleColor(G, node)
		for colorAv in colorsAv:

			colormapTemp = []
			G.nodes[node]['color'] = colorAv
			color = nx.get_node_attributes(G,'color')
			for node in G.nodes():
				colormapTemp.append(color[node])
			if scorefunctie is 1:
				if maxScore > scoreCounter1(G, colormapTemp):
					colormap = colormapTemp
			if scorefunctie is 2:
				if maxScore > scoreCounter2(G, colormapTemp):
					colormap = colormapTemp
			if scorefunctie is 3:
				if maxScore > scoreCounter3(G, colormapTemp):
					colormap = colormapTemp
			if scorefunctie is 4:
				if maxScore > scoreCounter4(G, colormapTemp):
					colormap = colormapTemp
	return colormap

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
		if kleur == 'black':
			score=6666666
			return score

	kleuren = []
	kleuren.append(red)
	kleuren.append(green)
	kleuren.append(blue)
	kleuren.append(yellow)
	kleuren.append(orange)
	kleuren.append(purple)
	kleuren.append(grey)
	# print(kleuren)
	bubbleSort(kleuren)
	# print(kleuren)
	score += kleuren[0]*12
	score += kleuren[1]*26
	score += kleuren[2]*27
	score += kleuren[3]*30
	score += kleuren[4]*37
	score += kleuren[5]*39
	score += kleuren[6]*41
	return score

def scoreCounter2(G, colormap):
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
		if kleur == 'black':
			score=6666666
			return score

	kleuren = []
	kleuren.append(red)
	kleuren.append(green)
	kleuren.append(blue)
	kleuren.append(yellow)
	kleuren.append(orange)
	kleuren.append(purple)
	kleuren.append(grey)
	# print(kleuren)
	bubbleSort(kleuren)
	# print(kleuren)
	score += kleuren[0]*19
	score += kleuren[1]*20
	score += kleuren[2]*21
	score += kleuren[3]*23
	score += kleuren[4]*36
	score += kleuren[5]*37
	score += kleuren[6]*38
	return score

def scoreCounter3(G, colormap):
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
		if kleur == 'black':
			score=6666666
			return score

	kleuren = []
	kleuren.append(red)
	kleuren.append(green)
	kleuren.append(blue)
	kleuren.append(yellow)
	kleuren.append(orange)
	kleuren.append(purple)
	kleuren.append(grey)
	# print(kleuren)
	bubbleSort(kleuren)
	# print(kleuren)
	score += kleuren[0]*16
	score += kleuren[1]*17
	score += kleuren[2]*31
	score += kleuren[3]*33
	score += kleuren[4]*36
	score += kleuren[5]*56
	score += kleuren[6]*57
	return score

def scoreCounter4(G, colormap):
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
		if kleur == 'black':
			score=6666666
			return score

	kleuren = []
	kleuren.append(red)
	kleuren.append(green)
	kleuren.append(blue)
	kleuren.append(yellow)
	kleuren.append(orange)
	kleuren.append(purple)
	kleuren.append(grey)
	# print(kleuren)
	bubbleSort(kleuren)
	# print(kleuren)
	score += kleuren[0]*3
	score += kleuren[1]*34
	score += kleuren[2]*36
	score += kleuren[3]*39
	score += kleuren[4]*41
	score += kleuren[5]*43
	score += kleuren[6]*58
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

# geeft nu random kleur uit de lijst colorsAvailable
def createColor(G, node, colorsAvailable):

	# als er kleuren beschibkaar zijn, voeg een kleur toe
	if colorsAvailable != []:
		# kleur een node in van een specifieke kleur
		G.nodes[node]['color'] = random.choice(colorsAvailable)
	# als er geen kleur beschikbaar is, maak de node zwart
	else:
		G.nodes[node]['color'] = "black"

def random_node_list(G):

	list_1 = []
	list_2 = []

	for node in G.nodes():

		list_1.append(node)

	for i in range(25):
		rannie = random.choice(list_1)
		list_2.append(rannie)
		list_1.remove(rannie)
	print(list_2)
	return(list_2)


if __name__ == '__main__':
	main()