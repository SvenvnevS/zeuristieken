import csv
import sys
import io
import networkx as nx
import matplotlib.pyplot as plt
import random
import xlwt
import xlrd
from networkx.algorithms import bipartite
import numpy as np 

from Random import controleColor
from Random import createColor


def randRunner(G, cost_table):
	



#gaat een lijst bouwen van toegestane kleuren van de node


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

