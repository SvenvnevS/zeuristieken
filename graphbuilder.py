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
	with open("UKRAINE/nodes.csv", 'r') as csvfile:
		plots = csv.reader(csvfile, delimiter=',')	
		for row in plots:
			G.add_node(str(row[0]),color='None')


	# lijnen tussen staten
	with open("UKRAINE/edges.csv", 'r') as csvfile:
		plots = csv.reader(csvfile, delimiter=',')	
		for row in plots:
			G.add_edge(str(row[0]),str(row[1]))

	# lees de oude score uit file
	
	colormap = []
	text = input("welke excel? score1.xls t/m score4.xls ")
	book = xlrd.open_workbook(text)
	sh = book.sheet_by_index(0)
	best_score = sh.cell_value(rowx = 0, colx = 0)
	for rows in sh.col(1):
		colormap.append(rows.value)
	del colormap[0]
	print(colormap)


	# 	# vraag de kleur op van een specifieke node
	# color = nx.get_node_attributes(G,'color')
	# for node in G.nodes():


	# 		# voeg de kleur toe in de array
	# 	colormap.append(color[node])



	# print(nx.info(G))
	print(best_score)


# geeft nu random kleur uit de lijst colorsAvailable


	nx.draw_networkx(G, with_labels=True,node_color=colormap)
	plt.title(text)
	plt.show()



if __name__ == '__main__':
	main()