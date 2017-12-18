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
from scorecalculator import scoreCounter
from Random import controleColor


score_array = []

def greed(G, iterations, cost_schedule, land):

	colormap = []

	# vraag de kleur op van een specifieke node
	color = nx.get_node_attributes(G,'color')
	for node in G.nodes():
		# voeg de kleur toe in de array
		colormap.append(color[node])

	# bereken de score
	tScore = scoreCounter(G, cost_schedule)

	loopA = iterations
	for i in range(loopA):
		G = greedy(G, colormap, cost_schedule, tScore)
		tScore, Temp = scoreCounter(G, cost_schedule)

		score_array.append(tScore)
		print("score ", tScore)

	excel_writer_greedy(score_array, land)

	return G, tScore
# end of main

def greedy(G, colormap, cost_schedule, maxScore):

	# roep een lijst aan met alle provincies in random volgorde
	random_nodes = random_node_list(G)
	for node in random_nodes:
		
		# kijk voor die node welke kleuren er mogen veranderen
		colorsAv = controleColor(G, node)
		for colorAv in colorsAv:

			colormapTemp = []

			# voldoe aan contain van niet dezelfde kleur als de buren
			if colorAv is not None:
				G.nodes[node]['color'] = colorAv
			else:
				G.nodes[node]['color'] = 'black'

			color = nx.get_node_attributes(G,'color')
			return G

#gaat een lijst bouwen van toegestane kleuren van de node

def random_node_list(G):

	list_1 = []
	list_2 = []

	for node in G.nodes():

		list_1.append(node)

	lengte = len(list_1) 
	for i in range(lengte):
		rannie = random.choice(list_1)
		list_2.append(rannie)
		list_1.remove(rannie)
	return(list_2)

def excel_writer_greedy(score_array, land):

	wb = xlwt.Workbook()
	
	ws = wb.add_sheet("Scores")

	for n in range(len(score_array)):

		ws.write(n, 0, n)
		ws.write(n, 1, score_array[n])
	destination = land + "/greedy_scores.xls"
	wb.save(destination)
