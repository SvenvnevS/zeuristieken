import numpy as np


def scoreCounter(G, cost_table):
	colormap = [G.nodes[node]['color'] for node in G.nodes()]

	kleur_labels = {'red': 		0,
					'green': 	1,
					'blue': 	2,
					'yellow': 	3,
					'orange': 	4,
					'purple': 	5,
					'grey': 	6,
					'black': 	7}

	kleuren = np.zeros(8)
	for kleur in colormap:
		kleuren[kleur_labels[kleur]] += 1

	# sort ascending
	kleuren = np.sort(kleuren)[::-1]

	total_costs = np.sum(COSTS[cost_table] * kleuren)


	return total_costs, colormap


# The cost table provided by Daan...
COSTS = np.array([ [12, 26, 27, 30, 37, 39, 41, 666],
	               [19, 20, 21, 23, 36, 37, 38, 666],
	               [16, 17, 31, 33, 36, 56, 57, 666],
	               [3, 34, 36, 39, 41, 43, 58, 666]])


