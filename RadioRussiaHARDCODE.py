import os, sys
import networkx as nx
import matplotlib.pyplot as plt

parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# print(parent_dir_name)
sys.path.append(parent_dir_name + "/zeuristieken/")
sys.path.append(parent_dir_name + "/zeuristieken/Algoritmes/")
sys.path.append(parent_dir_name + "/zeuristieken/Algoritmes/Random")


from scorecalculator import scoreCounter
from dataLoader import dataLoader
from dataLoader import dataWriter
from Random import rand
from hill import hillclimber
from greedy import greed



def main():

	# maak een random indeling
	land = "UKRAINE"
	nodescsv = land + "/nodes.csv"
	edgescsv = land + "/edges.csv"

	G = dataLoader(nodescsv, edgescsv)
	G = rand(G)
	
	cost_table = 2

	# bereken de score
	total_costs, colormap = scoreCounter(G, cost_table)

	destination = land + "/hiScore.xls"
	algo = "greedy"
	if algo == 'random':
		# show de random indeling
		dataWriter(G, destination, cost_table, total_costs, algo)
		nx.draw_networkx(G, with_labels=True,node_color=colormap)
		plt.show()

	if algo == 'greedy':
		iter = 5
		# # draai hillclimber x aantal keer
		G, score = greed(G, iter, cost_table)
		total_costs, colormap = scoreCounter(G, cost_table)
		dataWriter(G, destination, cost_table, total_costs, algo)

		nx.draw_networkx(G, with_labels=True,node_color=colormap)
		plt.show()
	if algo == 'hillclimber':
		iter = int(input("how many iterations? "))
		G, score = hillclimber(G, iter, cost_table)
		total_costs, colormap = scoreCounter(G, cost_table)
		dataWriter(G, destination, cost_table, total_costs, algo)

		nx.draw_networkx(G, with_labels=True,node_color=colormap)
		plt.show()

if __name__ == '__main__':
	main()	
