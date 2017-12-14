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

def hillOld(G, iterations, cost_schedule):
	colormap = []

	# vraag de kleur op van een specifieke node
	color = nx.get_node_attributes(G,'color')
	for node in G.nodes():
		# voeg de kleur toe in de array
		colormap.append(color[node])

	# bereken de score
	tScore = scoreCounter(G, cost_schedule)
	print(tScore, " score")

	loopA = iterations
	for i in range(loopA):
		G = hillclimber(G, colormap, cost_schedule, tScore)
		tScore = scoreCounter(G, cost_schedule)
		print(tScore, " scoreF1")

	return G, tScore
# end of main

def hillclimber(G, colormap, cost_schedule, maxScore):

	# roep een lijst aan met alle provincies in random volgorde

	random_nodes = random_node_list(G)
	for node in random_nodes:
		
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


# geeft nu random kleur uit de lijst colorsAvailable


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
	print(list_2)
	return(list_2)
