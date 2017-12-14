'''
This program can take the layouts stored in score excel files and builds the color+node layout from them
'''
import os, sys
import networkx as nx
import matplotlib.pyplot as plt
import csv
import io
import xlrd

parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# print(parent_dir_name)
sys.path.append(parent_dir_name + "/zeuristieken/")
sys.path.append(parent_dir_name + "/zeuristieken/Algoritmes")

from scorecalculator import scoreCounter


G = nx.Graph()
# nodes neerzetten per provincie
land = input("welk land wil je plotten? (RUSSIA/UKRAINE/USA) ")
# land = "USA"
destination = land + "/hiScore.xls"
edgescsv = land + "/edges.csv"
book = xlrd.open_workbook(destination)
sh = book.sheet_by_index(0)
n=0

for rows in sh.col(0):
	G.add_node(str(rows.value),color=sh.col(1)[n].value)
	n+=1

G.remove_node(str(sh.col(0)[0].value))
cost_table = int(sh.col(0)[0].value - 1)

# lijnen tussen staten
with open(edgescsv, 'r') as csvfile:
	plots = csv.reader(csvfile, delimiter=',')	
	for row in plots:
		G.add_edge(str(row[0]),str(row[1]))

# lees de oude score uit file
total_costs, colormap = scoreCounter(G, cost_table)


title = land + " Score " + str(total_costs)
nx.draw_networkx(G, with_labels=True,node_color=colormap)
plt.title(title)
plt.show()

