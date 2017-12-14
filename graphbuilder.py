'''
This program can take the layouts stored in score excel files and builds the color+node layout from them
'''
import sys
import csv
import io
import networkx as nx
import matplotlib.pyplot as plt
import random
import xlwt
import xlrd
from networkx.algorithms import bipartite



def main():
	G = nx.Graph()
	# nodes neerzetten per provincie
	text = input("welke excel? ")
	book = xlrd.open_workbook(text)
	sh = book.sheet_by_index(0)
	n=0
	for rows in sh.col(0):

		G.add_node(str(rows.value),color=sh.col(1)[n].value)
		n+=1
	G.remove_node(str(sh.col(0)[0].value))

	# lijnen tussen staten
	with open("UKRAINE/edges.csv", 'r') as csvfile:
		plots = csv.reader(csvfile, delimiter=',')	
		for row in plots:
			G.add_edge(str(row[0]),str(row[1]))

	# lees de oude score uit file
	
	colormap = []
	color = nx.get_node_attributes(G,'color')
	for node in G.nodes():
		# voeg de kleur toe in de array
		colormap.append(color[node])


	# 	# vraag de kleur op van een specifieke node
	# color = nx.get_node_attributes(G,'color')
	# for node in G.nodes():


	# 		# voeg de kleur toe in de array
	# 	colormap.append(color[node])



	# print(nx.info(G))


# geeft nu random kleur uit de lijst colorsAvailable


	nx.draw_networkx(G, with_labels=True,node_color=colormap)
	plt.title(text)
	plt.show()



if __name__ == '__main__':
	main()