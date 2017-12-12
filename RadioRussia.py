import os, sys

parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
print(parent_dir_name)
sys.path.append(parent_dir_name + "/zeuristieken/")
sys.path.append(parent_dir_name + "/zeuristieken/Algoritmes/")
sys.path.append(parent_dir_name + "/zeuristieken/Algoritmes/Random")


from dataLoader import random
from hill import scoreCounter
from hill import hillclimber


def main():
	G = random("UKRAINE/nodes.csv", "UKRAINE/edges.csv")
	print(scoreCounter(G, 0))
	G, score = hillclimber(G, 1000)
	print(scoreCounter(G, 0))

	# plot_network(G)

if __name__ == '__main__':
	main()	
