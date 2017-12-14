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
import copy
import numpy as np

from scorecalculator import scoreCounter


beste_score = 1000
score_array = []
beste_scores = [6666]
alle_scores = []




# def main():

# 	G = nx.Graph()
# 	# H = nx.Graph()

# 	# nodes neerzetten per provincie
# 	with open('nodes.csv', 'r') as csvfile:
# 		plots = csv.reader(csvfile, delimiter=',')	
# 		for row in plots:
# 			G.add_node(str(row[0]),color='None')

# 	# lijnen tussen staten
# 	with open('edges.csv', 'r') as csvfile:
# 		plots = csv.reader(csvfile, delimiter=',')	
# 		for row in plots:
# 			G.add_edge(str(row[0]),str(row[1]))

# 	# lees de oude score uit file
	
# 	# for i in range(5):
# 	for node in G.nodes():
# 		# voeg kleur aan een node toe die de buren nog niet hebben
# 		createColor(G, node, controleColor(G, node))


# 	colormap = []

# 	# vraag de kleur op van een specifieke node
# 	color = nx.get_node_attributes(G,'color')
# 	for node in G.nodes():
# 		# voeg de kleur toe in de array
# 		colormap.append(color[node])

# 	# bereken de score
# 	tScore1 = scoreCounter1(G, colormap)
# 	print(tScore1, " score1")
# 	tScore1 = scoreCounter(G, colormap, 0)
# 	print(tScore1, " score1")
	# tScore2 = scoreCounter2(G, colormap)
	# print(tScore2, " score2")
	# tScore3 = scoreCounter3(G, colormap)
	# print(tScore3, " score3")
	# tScore4 = scoreCounter4(G, colormap)
	# print(tScore4, " score4")

	# G, hill_score = hillclimber(G, 1000)	
	# print(hill_score)

	# 	loopA = 10
	# 	for i in range(loopA):

	# 		if tScore1 < tScore2 and tScore1 < tScore3 and tScore1 < tScore4:
	# 			colormap = hillclimber(G, colormap, 1, tScore1, i , loopA)
	# 			tScore1 = scoreCounter1(G, colormap)
	# 			print(tScore1, " scoreF1")

	# 		if tScore2 < tScore1 and tScore2 < tScore3 and tScore2 < tScore4:

	# 			colormap = hillclimber(G, colormap, 2, tScore2, i , loopA)

	# 			tScore2 = scoreCounter2(G, colormap)


	# 			score_array.append(tScore2)

	# 			alle_scores.append(tScore2)

	# 			if tScore2 < score_array[0]:
	# 				beste_scores.append(tScore2)

	# 				score_array.sort()

	# 				# open worksheet
	# 				wb = xlwt.Workbook()
	# 				# add sheet
	# 				ws = wb.add_sheet("beste_Scores")

	# 				n = 1
	# 				for node in G.nodes():

	# 					ws.write(n,0, node)
	# 					ws.write(n,1, color[node])
	# 					n+=1
	# 				# write in cel 0 , 0
	# 				ws.write(0,0, tScore2)
	# 				wb.save("beste_scores.xls")


	# 			print(tScore2, " scoreF2")


	# 		if tScore3 < tScore1 and tScore3 < tScore2 and tScore3 < tScore4:
	# 			colormap = hillclimber(G, colormap, 3, tScore3, i , loopA)
	# 			tScore3 = scoreCounter3(G, colormap)
	# 			print(tScore3, " scoreF3")

	# 			# t score is de score uit random
	# 		if tScore4 < tScore1 and tScore4 < tScore2 and tScore4 < tScore3:
	# 			colormap = hillclimber(G, colormap, 4, tScore4, i , loopA)
	# 			tScore4 = scoreCounter4(G, colormap)
	# 			print(tScore4, " scoreF4")


	# 	print(alle_scores)

	# 	n = 0
	# 	wb = xlwt.Workbook()
	# 		# add sheet
	# 	ws = wb.add_sheet("Scores")

	# 	for score in range(len(alle_scores)):
	# 		ws.write(n,0, score)
	# 		ws.write(n,1, alle_scores[score])

	# 		n+=1

	# 	wb.save("hill_climber_scores.xls")

	# 	# nx.draw_networkx(G, with_labels=True,node_color=colormap)
	# 	# plt.show()
	# # end of main
	# 	beste_scores.sort()
	# 	print("de beste scores zijn {}" .format(beste_scores))

def randomSwap(G):

	# pick a random node
	random_node = random_node_list(G)[0]

	# check which colors are valid for this node
	valid_colors = controleColor(G, random_node)

	# give it a random valid color, if no valid color present make it black
	if valid_colors is not None:
		G.nodes[random_node]['color'] = np.random.choice(valid_colors)
	else:
		G.nodes[random_node]['color'] = 'black'

	return G


# def hillclimber(G, colormap, scorefunctie, oude_score, i, loopA):
def hillclimber(G, iterations, cost_schedule):
	# roep een lijst aan met alle provincies in random volgorde
	for iter in range(iterations):

		# calculate current temperture
		T = iterations - iter

		# store the old state
		old_G = copy.deepcopy(G)


		old_S, colormap = scoreCounter(old_G, cost_schedule)

		# randomly swap a node's color
		G = randomSwap(G)

		# get the new score
		new_S, colormap = scoreCounter(G, cost_schedule)

		# keep the new state if its an improvement

		if new_S <= old_S:

			alle_scores.append(new_S)

			if new_S < beste_scores[0]:
				beste_scores.append(new_S)
				beste_scores.sort()

				
				# open worksheet
				wb = xlwt.Workbook()
					# add sheet
				ws = wb.add_sheet("beste_Scores")

				n = 1
				color = nx.get_node_attributes(G,'color')
				
				for node in G.nodes():

					ws.write(n,0, node)
					ws.write(n,1, color[node])
					n+=1
				# write in cel 0 , 0
				ws.write(0,0, new_S)
				wb.save("beste_scores.xls")

			# print(new_S)
			old_S = new_S
			old_G = G




		elif sAnneal(T, old_S, new_S) == 1:
			alle_scores.append(new_S)

			print("ANEEALING DONEEEE")
			old_S = new_S
			old_G = G

		# go back to the previous state since it's worse
		else:
			G = old_G

	excel_writer(alle_scores)
	print(beste_scores)

	return G, old_S


def sAnneal(T, old_S, new_S):

	# print("JAAHAA")
	# print("T is {} " .format(T))
	# print ("old score is {}" .format(old_S))
		# print (new_S)


	check = math.e ** ((old_S - new_S) / T)
	print("check is {}".format(check))

	check2 = random.uniform(0, 1)

	if check > check2:
		return 1
	# return check > check

def excel_writer(score_array):

	
	print("KUT")
	wb = xlwt.Workbook()
	
	ws = wb.add_sheet("Scores")

	for n in range(len(score_array)):

		ws.write(n, 0, n)
		ws.write(n, 1, score_array[n])

	wb.save("hill_climber_scores.xls")






	# random_nodes = random_node_list(G)
	# for node in random_nodes:
		
	# 	colorsAv = controleColor(G, node)
		
	# 	colormapTemp = []

	# 	# voldoe aan contain van niet dezelfde kleur als de buren
	# 	if colorsAv is not None:
	# 		G.nodes[node]['color'] = colorsAv[0]
	# 		# print(colorAv)
	# 	else:
	# 		G.nodes[node]['color'] = 'black'


	# 	color = nx.get_node_attributes(G,'color')

	# 	for node in G.nodes():
	# 		colormapTemp.append(color[node])
		

	# 	if scorefunctie is 1:
	# 		new_score = scoreCounter1(G, colormapTemp)

	# 		if oude_score > new_score:
	# 			colormap = colormapTemp


	# 		else:
	# 			getal = sAnneal(G, colormapTemp, T, oude_score, new_score, i)
	# 			if getal is 1:
	# 				colormap = colormapTemp


		
	# 	if scorefunctie is 2:
	# 		new_score = scoreCounter2(G, colormapTemp)
	# 		print("NEW score {} " .format(new_score))

	# 		if oude_score > new_score:
	# 			colormap = colormapTemp
	# 			return colormap

	# 		else:
	# 			getal = sAnneal(G, colormapTemp, T, oude_score, new_score, i)
	# 			if getal is 1:
	# 				colormap = colormapTemp
	# 				return colormap





	# 	if scorefunctie is 3:
	# 		new_score = scoreCounter2(G, colormapTemp)

	# 		if oude_score > new_score:
	# 			colormap = colormapTemp

	# 		else:
	# 			getal = sAnneal(G, colormapTemp, T, oude_score, new_score, i)
	# 			if getal is 1:
	# 				colormap = colormapTemp
	# 	if scorefunctie is 4:
	# 		new_score = scoreCounter2(G, colormapTemp)

	# 		if oude_score > new_score:
	# 			colormap = colormapTemp

	# 		else:
	# 			getal = sAnneal(G, colormapTemp, T, oude_score, new_score, i)
	# 			if getal is 1:
	# 				colormap = colormapTemp

	# 	return colormap

# # The cost table provided by Daan...
# COSTS = np.array([ [12, 26, 27, 30, 37, 39, 41, 666],
# 	               [19, 20, 21, 23, 36, 37, 38, 666],
# 	               [16, 17, 31, 33, 36, 56, 57, 666],
# 	               [3, 34, 36, 39, 41, 43, 58, 666]])


# def scoreCounter(G, cost_table):
# 	colormap = [G.nodes[node]['color'] for node in G.nodes()]

# 	kleur_labels = {'red': 		0,
# 					'green': 	1,
# 					'blue': 	2,
# 					'yellow': 	3,
# 					'orange': 	4,
# 					'purple': 	5,
# 					'grey': 	6,
# 					'black': 	7}

# 	kleuren = np.zeros(8)
# 	for kleur in colormap:
# 		kleuren[kleur_labels[kleur]] += 1

# 	# sort ascending
# 	kleuren = np.sort(kleuren)[::-1]

# 	total_costs = np.sum(COSTS[cost_table] * kleuren)
# 	return total_costs

# 	# for kleur in colormap:
# 	# 	if kleur == 'red':
# 	# 		red+=1
# 	# 	if kleur == 'green':
# 	# 		green+=1
# 	# 	if kleur == 'blue':
# 	# 		blue+=1
# 	# 	if kleur == 'yellow':
# 	# 		yellow+=1
# 	# 	if kleur == 'orange':
# 	# 		orange+=1
# 	# 	if kleur == 'purple':
# 	# 		purple+=1
# 	# 	if kleur == 'grey':
# 	# 		grey+=1
# 	# 	if kleur == 'black':
# 	# 		score=6666666
# 	# 		return score

# # telt totaal score gebaseerd op kosten tabel 1
# def scoreCounter1(G, colormap):
# 	score = 0
# 	red = 0
# 	green = 0
# 	blue = 0
# 	yellow = 0
# 	orange = 0
# 	purple = 0
# 	grey = 0

# 	for kleur in colormap:
# 		if kleur == 'red':
# 			red+=1
# 		if kleur == 'green':
# 			green+=1
# 		if kleur == 'blue':
# 			blue+=1
# 		if kleur == 'yellow':
# 			yellow+=1
# 		if kleur == 'orange':
# 			orange+=1
# 		if kleur == 'purple':
# 			purple+=1
# 		if kleur == 'grey':
# 			grey+=1
# 		if kleur == 'black':
# 			score=6666666
# 			return score

# 	kleuren = []
# 	kleuren.append(red)
# 	kleuren.append(green)
# 	kleuren.append(blue)
# 	kleuren.append(yellow)
# 	kleuren.append(orange)
# 	kleuren.append(purple)
# 	kleuren.append(grey)
# 	# print(kleuren)
# 	bubbleSort(kleuren)
# 	# print(kleuren)
# 	score += kleuren[0]*12
# 	score += kleuren[1]*26
# 	score += kleuren[2]*27
# 	score += kleuren[3]*30
# 	score += kleuren[4]*37
# 	score += kleuren[5]*39
# 	score += kleuren[6]*41
# 	return score

# def scoreCounter2(G, colormap):
# 	score = 0
# 	red = 0
# 	green = 0
# 	blue = 0
# 	yellow = 0
# 	orange = 0
# 	purple = 0
# 	grey = 0

# 	for kleur in colormap:
# 		if kleur == 'red':
# 			red+=1
# 		if kleur == 'green':
# 			green+=1
# 		if kleur == 'blue':
# 			blue+=1
# 		if kleur == 'yellow':
# 			yellow+=1
# 		if kleur == 'orange':
# 			orange+=1
# 		if kleur == 'purple':
# 			purple+=1
# 		if kleur == 'grey':
# 			grey+=1
# 		if kleur == 'black':
# 			score=6666666
# 			return score

# 	kleuren = []
# 	kleuren.append(red)
# 	kleuren.append(green)
# 	kleuren.append(blue)
# 	kleuren.append(yellow)
# 	kleuren.append(orange)
# 	kleuren.append(purple)
# 	kleuren.append(grey)
# 	# print(kleuren)
# 	bubbleSort(kleuren)
# 	# print(kleuren)
# 	score += kleuren[0]*19
# 	score += kleuren[1]*20
# 	score += kleuren[2]*21
# 	score += kleuren[3]*23
# 	score += kleuren[4]*36
# 	score += kleuren[5]*37
# 	score += kleuren[6]*38
# 	return score

# def scoreCounter3(G, colormap):
# 	score = 0
# 	red = 0
# 	green = 0
# 	blue = 0
# 	yellow = 0
# 	orange = 0
# 	purple = 0
# 	grey = 0

# 	for kleur in colormap:
# 		if kleur == 'red':
# 			red+=1
# 		if kleur == 'green':
# 			green+=1
# 		if kleur == 'blue':
# 			blue+=1
# 		if kleur == 'yellow':
# 			yellow+=1
# 		if kleur == 'orange':
# 			orange+=1
# 		if kleur == 'purple':
# 			purple+=1
# 		if kleur == 'grey':
# 			grey+=1
# 		if kleur == 'black':
# 			score=6666666
# 			return score

# 	kleuren = []
# 	kleuren.append(red)
# 	kleuren.append(green)
# 	kleuren.append(blue)
# 	kleuren.append(yellow)
# 	kleuren.append(orange)
# 	kleuren.append(purple)
# 	kleuren.append(grey)
# 	# print(kleuren)
# 	bubbleSort(kleuren)
# 	# print(kleuren)
# 	score += kleuren[0]*16
# 	score += kleuren[1]*17
# 	score += kleuren[2]*31
# 	score += kleuren[3]*33
# 	score += kleuren[4]*36
# 	score += kleuren[5]*56
# 	score += kleuren[6]*57
# 	return score

# def scoreCounter4(G, colormap):
# 	score = 0
# 	red = 0
# 	green = 0
# 	blue = 0
# 	yellow = 0
# 	orange = 0
# 	purple = 0
# 	grey = 0

# 	for kleur in colormap:
# 		if kleur == 'red':
# 			red+=1
# 		if kleur == 'green':
# 			green+=1
# 		if kleur == 'blue':
# 			blue+=1
# 		if kleur == 'yellow':
# 			yellow+=1
# 		if kleur == 'orange':
# 			orange+=1
# 		if kleur == 'purple':
# 			purple+=1
# 		if kleur == 'grey':
# 			grey+=1
# 		if kleur == 'black':
# 			score=6666666
# 			return score

# 	kleuren = []
# 	kleuren.append(red)
# 	kleuren.append(green)
# 	kleuren.append(blue)
# 	kleuren.append(yellow)
# 	kleuren.append(orange)
# 	kleuren.append(purple)
# 	kleuren.append(grey)
# 	# print(kleuren)
# 	bubbleSort(kleuren)
# 	# print(kleuren)
# 	score += kleuren[0]*3
# 	score += kleuren[1]*34
# 	score += kleuren[2]*36
# 	score += kleuren[3]*39
# 	score += kleuren[4]*41
# 	score += kleuren[5]*43
# 	score += kleuren[6]*58
# 	return score

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

	for i in range(len(list_1)):
		rannie = random.choice(list_1)
		list_2.append(rannie)
		list_1.remove(rannie)
	# print(list_2)
	return list_2
	# print(G.nodes())
	# print(copy.deepcopy(G.nodes()))
	# print(random.shuffle(copy.deepcopy(G.nodes())))
	# shuffled_nodes = copy.deepcopy(G.nodes())
	# print(shuffled_nodes)
	# random.shuffle(shuffled_nodes)

	# return shuffled_nodes




if __name__ == '__main__':
	main()