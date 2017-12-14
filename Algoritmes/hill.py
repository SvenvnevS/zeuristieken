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
from Random import controleColor

beste_score = 1000
score_array = []
beste_scores = [6666]
alle_scores = []






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
def hillclimber(G, iterations, cost_schedule, land):
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

		if new_S < old_S:

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

			print(new_S)
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

	excel_writer(alle_scores, land)
	print(beste_scores)

	return G, old_S


def sAnneal(T, old_S, new_S):

	# print("JAAHAA")
	# print("T is {} " .format(T))
	print ("old score is {}" .format(old_S))
		# print (new_S)


	check = math.e ** ((new_S - old_S) / T)
	print("check is {}".format(check))

	check2 = random.uniform(0, 1)

	if check > check2:
		return 1

def excel_writer(score_array, land):

	wb = xlwt.Workbook()
	
	ws = wb.add_sheet("Scores")

	for n in range(len(score_array)):

		ws.write(n, 0, n)
		ws.write(n, 1, score_array[n])
	destination = land + "/hill_climber_scores.xls"
	wb.save(destination)






	

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




if __name__ == '__main__':
	main()