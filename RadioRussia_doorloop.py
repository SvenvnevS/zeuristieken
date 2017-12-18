import os, sys
import networkx as nx
import matplotlib.pyplot as plt
import xlwt
import xlrd

parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# print(parent_dir_name)
sys.path.append(parent_dir_name + "/zeuristieken/")
sys.path.append(parent_dir_name + "/zeuristieken/Algoritmes/")


from scorecalculator import scoreCounter
from dataLoader import dataLoader
from dataLoader import dataWriter
from Random import rand
from hillclimberdoorgaan import hillclimber
from greedydoorgaan import greed



def main():

	# maak een random indeling
	land = input("welk land wil je plotten? (RUSSIA/UKRAINE/USA) ")
	nodescsv = land + "/nodes.csv"
	edgescsv = land + "/edges.csv"

	G = dataLoader(nodescsv, edgescsv)
	G = rand(G)
	
	cost_table = int(input("welke kosten tabel? 1 t/m 4 "))-1

	# bereken de score
	total_costs, colormap = scoreCounter(G, cost_table)

	destination = land + "/hiScore.xls"
	algo = input('welke algoritme? (random/greedy/hillclimber) ')
	if algo == 'random':
		# show de random indeling
		dataWriter(G, destination, cost_table, total_costs, algo)
		title = land + " Score " + str(total_costs)
		nx.draw_networkx(G, with_labels=True,node_color=colormap)
		plt.title(title)
		plt.show()


	if algo == 'greedy':
		greed_nr = int(input("how many times do you want to run greedy? "))
		iter = int(input("how many iterations? "))
		# wb = xlwt.Workbook()
	
		# ws = wb.add_sheet("Scores", cell_overwrite_ok=True)
		for greed_i in range(greed_nr):
			G, score = greed(G, iter, cost_table, land, greed_i)
			total_costs, colormap = scoreCounter(G, cost_table)
			dataWriter(G, destination, cost_table, total_costs, algo)
			G = rand(G)

		

		# destin = land + "/greedy_scores.xls"
		# wb.save(destin)
		

	if algo == 'hillclimber':
		hill_nr = int(input("how many times do you want to run the hillclimber? "))
		iter = int(input("how many iterations? "))
		# wb = xlwt.Workbook()
	
		# ws = wb.add_sheet("Scores", cell_overwrite_ok=True)
		for hill_i in range(hill_nr):
			G, score = hillclimber(G, iter, cost_table, land, hill_i)
			total_costs, colormap = scoreCounter(G, cost_table)
			dataWriter(G, destination, cost_table, total_costs, algo)
			G = rand(G)

		# destin = land + "/hill_climber_scores.xls"
		# wb.save(destin)
		
if __name__ == '__main__':
	main()	
