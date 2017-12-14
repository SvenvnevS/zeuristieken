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

cost_table = 1

def main():

	# maak een random indeling
	G = random("UKRAINE/nodes.csv", "UKRAINE/edges.csv")
	
	# bereken de score
	total_costs, colormap = scoreCounter(G, cost_table)
	print("RANDOM" .format(total_costs))

	# show de random indeling
	# nx.draw_networkx(G, with_labels=True,node_color=colormap)
	# plt.show()


	# # draai hillclimber x aantal keer
	G, score = hillclimber(G, 1000, cost_table)

	
	total_costs, colormap = scoreCounter(G, cost_table)
	print(total_costs)

	nx.draw_networkx(G, with_labels=True,node_color=colormap)
	plt.show()


if __name__ == '__main__':
	main()	
