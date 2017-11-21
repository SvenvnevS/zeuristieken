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
	with open('nodes.csv', 'r') as csvfile:
		plots = csv.reader(csvfile, delimiter=',')	
		for row in plots:
			G.add_node(str(row[0]),color='None')


	# lijnen tussen staten
	with open('edges.csv', 'r') as csvfile:
		plots = csv.reader(csvfile, delimiter=',')	
		for row in plots:
			G.add_edge(str(row[0]),str(row[1]))

	# lees de oude score uit file
	
	book = xlrd.open_workbook("score.xls")
	sh = book.sheet_by_index(0)
	last_score = sh.cell_value(rowx = 0, colx = 0)
	print(last_score)


		
	for node in G.nodes():
		# voeg kleur aan een node toe die de buren nog niet hebben
		createColor(G, node, controleColor(G, node))


	colormap = []
	for node in G.nodes():

		# vraag de kleur op van een specifieke node
		color = nx.get_node_attributes(G,'color')

		# voeg de kleur toe in de array
		colormap.append(color[node])

	# bereken de score
	tScore = scoreCounter1(G, colormap)

	print(nx.info(G))

	print("score is: {}".format(tScore))


	if last_score > tScore:

		
		# open worksheet
		wb = xlwt.Workbook()
		# add sheet
		ws = wb.add_sheet("A Test Sheet")

		# write in cel 0 , 0
		ws.write(0,0, tScore)
		wb.save("score.xls")

	# teken de map
	# nx.draw_networkx(G, with_labels=True,node_color=colormap)

	plt.show()
# end of main


# telt totaal score gebaseerd op kosten tabel 1
def scoreCounter1(G, colormap):
	score = 0
	red = 0
	green = 0
	blue = 0
	yellow = 0
	orange = 0
	purple = 0
	grey = 0

	for kleur in colormap:
		if kleur == 'red':
			red+=1
		if kleur == 'green':
			green+=1
		if kleur == 'blue':
			blue+=1
		if kleur == 'yellow':
			yellow+=1
		if kleur == 'orange':
			orange+=1
		if kleur == 'purple':
			purple+=1
		if kleur == 'grey':
			grey+=1
		if kleur == 'black':
			return score = 66666

	kleuren = []
	kleuren.append(red)
	kleuren.append(green)
	kleuren.append(blue)
	kleuren.append(yellow)
	kleuren.append(orange)
	kleuren.append(purple)
	kleuren.append(grey)
	print(kleuren)
	bubbleSort(kleuren)
	print(kleuren)
	score += kleuren[0]*12
	score += kleuren[1]*26
	score += kleuren[2]*27
	score += kleuren[3]*30
	score += kleuren[4]*37
	score += kleuren[5]*39
	score += kleuren[6]*41
	return score

#gaat een lijst bouwen van toegestane kleuren van de node
def controleColor(G, province):

	kleuren = ""
	colorsAvailable = []

	# vraagt van een node de buren op
	neighbors = G[province]


	for neighbor in neighbors:

		# vraag per provincie de huidige kleur op
	 	colr=nx.get_node_attributes(G,'color')
	 	

	 	# vraag de kleuren op van de buren van een provincie
	 	kleuren += (colr[neighbor])
	 	
	if 'grey' not in kleuren:
		colorsAvailable.append('grey')
	if 'red' not in kleuren:
		colorsAvailable.append('red')
	if 'green' not in kleuren:
		colorsAvailable.append('green')
	if 'blue' not in kleuren:
		colorsAvailable.append('blue')
	if 'yellow' not in kleuren:
		colorsAvailable.append('yellow')
	if 'orange' not in kleuren:
		colorsAvailable.append('orange')
	if 'purple' not in kleuren:
		colorsAvailable.append('purple')
	return colorsAvailable

# copied from http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]<alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

# geeft nu random kleur uit de lijst colorsAvailable
def createColor(G, node, colorsAvailable):
	if colorsAvailable is not None
		# kleur een node in van een specifieke kleur
		G.nodes[node]['color'] = random.choice(colorsAvailable)
	else 
		G.nodes[node]['color'] = "black"


if __name__ == '__main__':
	main()