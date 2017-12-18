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
def hillclimber(G, iterations, cost_schedule, land, ws, hill_i):
	# roep een lijst aan met alle provincies in random volgorde
	# for i in range (10):
	best_G = copy.deepcopy(G)
	
	alle_scores = []
	for iter in range(iterations):

		# calculate lineair current temperture
		# T = iterations - iter
		
		# EXPONENTIAL
		T = iterations * (0.995 ** (iter * 30))
		# print("LINEAIR {}" .format(T))
		# print("EXPONENTIEEL {}" .format(T2))
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
				best_G = copy.deepcopy(G)

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

	excel_writer(alle_scores, land, ws, hill_i, iterations)
	print(beste_scores)

	return best_G, old_S


def sAnneal(T, old_S, new_S):

	# print("JAAHAA")
	print("T is {} " .format(T))
	print ("old score is {}" .format(old_S))
	print ("new score is {}" .format(new_S))


	check = math.e ** (-(new_S - old_S) / T)
	print("check is {}".format(check))

	check2 = random.uniform(0, 1)

	if check > check2:
		return 1

def excel_writer(score_array, land, ws, hill_i, iter):


	for n in range(len(score_array)):

		ws.write(n, hill_i*2, n)
		ws.write(n, hill_i*2+1, score_array[n])

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