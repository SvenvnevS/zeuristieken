import networkx as nx
import csv
import xlwt
import xlrd
import os, sys

def dataLoader(file_a, file_b):
	G = nx.Graph()

	# nodes neerzetten per provincie
	with open(file_a, 'r') as csvfile:
		plots = csv.reader(csvfile, delimiter=',')	
		for row in plots:
			G.add_node(str(row[0]),color='None')

	# lijnen tussen staten
	with open(file_b, 'r') as csvfile:
		plots = csv.reader(csvfile, delimiter=',')	
		for row in plots:
			G.add_edge(str(row[0]),str(row[1]))
	return G

def dataWriter(G, destination, cost_table, tScore, algo):

	color = nx.get_node_attributes(G,'color')
	book = xlrd.open_workbook(destination)
	sh = book.sheet_by_index(0)
	n=0
	prevScore = sh.cell_value(rowx = 0, colx = 1)
	if tScore < prevScore:
		print("new highscore for this country, saving to {}".format(destination))
		wb = xlwt.Workbook()
	
		ws = wb.add_sheet("Score")

		n = 1
		for node in G.nodes():
			ws.write(n,0, node)
			ws.write(n,1, color[node])
			n+=1

		ws.write(0,2, algo + " algoritme")
		ws.write(0,1, tScore)
		ws.write(0,0, cost_table+1)
		wb.save(destination)

