import os, sys
import networkx as nx
import matplotlib.pyplot as plt

parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# print(parent_dir_name)
sys.path.append(parent_dir_name + "/zeuristieken/")
sys.path.append(parent_dir_name + "/zeuristieken/Algoritmes/")
sys.path.append(parent_dir_name + "/zeuristieken/Algoritmes/Random")


from scorecalculator import scoreCounter
from dataLoader import random
from hill import hillclimber
from greedy import greed



def main():

	# maak een random indeling
	land = input("welk land wil je plotten? (RUSSIA/UKRAINE/USA) ")
	nodescsv = land + "/nodes.csv"
	edgescsv = land + "/edges.csv"
	G = random(nodescsv, edgescsv)
	
	cost_table = int(input("welke kosten tabel? 1 t/m 4 "))-1
	# bereken de score
	total_costs, colormap = scoreCounter(G, cost_table)

	algo = input('welke algoritme? (random/greedy/hillclimber) ')
	if algo == 'random':
		# show de random indeling
		nx.draw_networkx(G, with_labels=True,node_color=colormap)
		plt.show()

	if algo == 'greedy':
		iter = int(input("how many iterations? "))
		# # draai hillclimber x aantal keer
		G, score = greed(G, iter, cost_table)
		total_costs, colormap = scoreCounter(G, cost_table)

		nx.draw_networkx(G, with_labels=True,node_color=colormap)
		plt.show()
	if algo == 'hillclimber':
		iter = int(input("how many iterations? "))
		G, score = hillclimber(G, iter, cost_table)
		total_costs, colormap = scoreCounter(G, cost_table)

		nx.draw_networkx(G, with_labels=True,node_color=colormap)
		plt.show()

if __name__ == '__main__':
	main()	
