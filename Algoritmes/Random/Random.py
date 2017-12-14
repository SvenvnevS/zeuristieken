import csv
import networkx as nx
import matplotlib.pyplot as plt
import random
from networkx.algorithms import bipartite

def rand(G):
	for node in G.nodes():
		# voeg kleur aan een node toe die de buren nog niet hebben
		createColor(G, node, controleColor(G, node))
	return G


def createColor(G, node, colorsAvailable):

	# als er kleuren beschibkaar zijn, voeg een kleur toe
	if colorsAvailable != []:
		# kleur een node in van een specifieke kleur
		G.nodes[node]['color'] = random.choice(colorsAvailable)
	# als er geen kleur beschikbaar is, maak de node zwart
	else:
		G.nodes[node]['color'] = "black"

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