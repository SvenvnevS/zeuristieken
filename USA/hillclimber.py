import csv
import sys
import io
import networkx as nx
import matplotlib.pyplot as plt
import random
import xlwt
import xlrd
import math
from networkx.algorithms import bipartite

beste_score = 1000
score_array = []
beste_scores = []
def main():

	G = nx.Graph()
	# H = nx.Graph()

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

	loopA = 50

	for i in range(loopA):


		# bekijk wat de hoogste random score heeft gekregen en ga daarmee de hillclimber in
		if tScore1 < tScore2 and tScore1 < tScore3 and tScore1 < tScore4: 

# JE GAAT HILLCLUMBER ALTIJD IN MET DE HOOGSTE SCORE

			colormap = hillclimber(G, colormap, 1, tScore1, i, loopA)

			# overschrijf de oude random score met de nieuwe hillclimber score 
			tScore1 = scoreCounter1(G, colormap)
			print(tScore1, " scoreF1")

		if tScore2 < tScore1 and tScore2 < tScore3 and tScore2 < tScore4:
			colormap = hillclimber(G, colormap, 2, tScore2, i , loopA)
			tScore2 = scoreCounter2(G, colormap)

			# VOEG ALLE NIEUWE BESTE SCORES TOE AAN ARRAY
			score_array.append(tScore2)

			if tScore2 < score_array[0]:
	
					beste_scores.append(tScore2)

			score_array.sort()


			print(tScore2, " scoreF2")


		if tScore3 < tScore1 and tScore3 < tScore2 and tScore3 < tScore4:
			colormap = hillclimber(G, colormap, 3, tScore3, i , loopA)
			tScore3 = scoreCounter3(G, colormap)
			print(tScore3, " scoreF3")

			# t score is de score uit random
		if tScore4 < tScore1 and tScore4 < tScore2 and tScore4 < tScore3:
			colormap = hillclimber(G, colormap, 4, tScore4, i , loopA)
			tScore4 = scoreCounter4(G, colormap)
			print(tScore4, " scoreF4")

	# nx.draw_networkx(G, with_labels=True,node_color=colormap)
	# plt.show()
# end of main

	beste_scores.sort()
	print("de beste scores zijn {}" .format(beste_scores))
	# print(score_array)

def hillclimber(G, colormap, scorefunctie, oudeScore, i , loopA):

	
	T = loopA * (0.995 ** (i*20))
	# roep een lijst aan met alle provincies in random volgorde
	random_nodes = random_node_list(G)

	# ga random nodes langs
	for node in random_nodes:
		
		# vraag een lijst op van die specifieke node, welke andere kleuren die node zou kunnen krijgen
		colorsAv = controleColor(G, node)

		# voor iedere kleur in de kleurenlijst
		for colorAv in colorsAv:

			colormapTemp = []

			# vul de node met die kleur
			if colorAv is not None:
				G.nodes[node]['color'] = colorAv
			else:
				G.nodes[node]['color'] = 'black'

			# vraag de kleur op van alle nodes 
			color = nx.get_node_attributes(G,'color')

			for node in G.nodes():

				# voeg de kleur van die node toe aan de array
				colormapTemp.append(color[node])


			# if scorefunctie is 1:
			# 	if oudeScore > scoreCounter1(G, colormapTemp):
			# 		colormap = colormapTemp



			# als uit de 4 random kostentabellen, tabel 2 het beste was, wordt hillclimber aangeroepen met 2 
			if scorefunctie is 2:

				# als de nieuwe score beter is dan de vorige score, houd deze dan. Anders Allealing
				new_score = scoreCounter2(G, colormapTemp)
				if  new_score < oudeScore:
					colormap = colormapTemp
				else:
					getal = sAnneal(G, colormapTemp, loopA, T, oudeScore, i)
					if getal is 1:
						colormap = colormapTemp


			# if scorefunctie is 3:
			# 	if oudeScore > scoreCounter3(G, colormapTemp):
			# 		colormap = colormapTemp
			# if scorefunctie is 4:
			# 	if oudeScore > scoreCounter4(G, colormapTemp):
			# 		colormap = colormapTemp
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

	for i in range(51):
		rannie = random.choice(list_1)
		list_2.append(rannie)
		list_1.remove(rannie)
	# print(list_2)
	return(list_2)

def sAnneal(G, colormapTemp, loopA, T, oudeScore, i):


	# bereken de nieuwe score nadat er 1 node zijn kleur is aangepast
	scoreNew = scoreCounter2(G,colormapTemp)

	# gebruik de 1e keer 1000 als beste score. daarna de beste score tot dantoe gevonden
	# if i is 0:
	check1 = math.e ** ((beste_score-scoreNew) / T) 
		# print("done")
	# else:
	# 	bestuu_score = score_array[0]
	# 	check1 = math.e ** ((bestuu_score-scoreNew) / T) 

	check2 = random.uniform(0, 1)

	# als de nieuwe score niet te slecht is, gaan we met die score verder
	if check1 > check2:

		return 1
if __name__ == '__main__':
	main()