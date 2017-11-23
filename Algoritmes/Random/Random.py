import csv
import sys
import io
import networkx as nx
import matplotlib.pyplot as plt
import random
import xlwt
import xlrd
from networkx.algorithms import bipartite


def main():

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")
	for kipsate in range(100000):
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
		
		book = xlrd.open_workbook("score1.xls")
		sh = book.sheet_by_index(0)
		last_score1 = sh.cell_value(rowx = 0, colx = 0)
		book = xlrd.open_workbook("score2.xls")
		sh = book.sheet_by_index(0)
		last_score2 = sh.cell_value(rowx = 0, colx = 0)
		book = xlrd.open_workbook("score3.xls")
		sh = book.sheet_by_index(0)
		last_score3 = sh.cell_value(rowx = 0, colx = 0)
		book = xlrd.open_workbook("score4.xls")
		sh = book.sheet_by_index(0)
		last_score4 = sh.cell_value(rowx = 0, colx = 0)


			
		for node in G.nodes():
			# voeg kleur aan een node toe die de buren nog niet hebben
			createColor(G, node, controleColor(G, node))


		colormap = []

		# vraag de kleur op van een specifieke node
		color = nx.get_node_attributes(G,'color')
		for node in G.nodes():


			# voeg de kleur toe in de array
			colormap.append(color[node])

		# bereken de score
		tScore1 = scoreCounter1(G, colormap)
		tScore2 = scoreCounter2(G, colormap)
		tScore3 = scoreCounter3(G, colormap)
		tScore4 = scoreCounter4(G, colormap)

		# print(nx.info(G))

		# print("score is: {}".format(tScore))


		if last_score1 > tScore1:

			
			# open worksheet
			wb = xlwt.Workbook()
			# add sheet
			ws = wb.add_sheet("Scores")

			n = 1
			for node in G.nodes():
				ws.write(n,0, node)
				ws.write(n,1, color[node])
				n+=1
			# write in cel 0 , 0
			ws.write(0,0, tScore1)
			wb.save("score1.xls")

		if last_score2 > tScore2:

			
			# open worksheet
			wb = xlwt.Workbook()
			# add sheet
			ws = wb.add_sheet("Scores")

			n = 1
			for node in G.nodes():
				ws.write(n,0, node)
				ws.write(n,1, color[node])
				n+=1
			# write in cel 0 , 0
			ws.write(0,0, tScore2)
			wb.save("score2.xls")

		if last_score3 > tScore3:

			
			# open worksheet
			wb = xlwt.Workbook()
			# add sheet
			ws = wb.add_sheet("Scores")

			n = 1
			for node in G.nodes():
				ws.write(n,0, node)
				ws.write(n,1, color[node])
				n+=1
			# write in cel 0 , 0
			ws.write(0,0, tScore3)
			wb.save("score3.xls")

		if last_score4 > tScore4:

			
			# open worksheet
			wb = xlwt.Workbook()
			# add sheet
			ws = wb.add_sheet("Scores")

			n = 1
			for node in G.nodes():
				ws.write(n,0, node)
				ws.write(n,1, color[node])
				n+=1
			# write in cel 0 , 0
			ws.write(0,0, tScore4)
			wb.save("score4.xls")

		# teken de map
		# nx.draw_networkx(G, with_labels=True,node_color=colormap)

		# plt.show()
	# end of main
		print(kipsate)


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
			score=6666666
			return score

	kleuren = []
	kleuren.append(red)
	kleuren.append(green)
	kleuren.append(blue)
	kleuren.append(yellow)
	kleuren.append(orange)
	kleuren.append(purple)
	kleuren.append(grey)
	# print(kleuren)
	bubbleSort(kleuren)
	# print(kleuren)
	score += kleuren[0]*12
	score += kleuren[1]*26
	score += kleuren[2]*27
	score += kleuren[3]*30
	score += kleuren[4]*37
	score += kleuren[5]*39
	score += kleuren[6]*41
	return score

def scoreCounter2(G, colormap):
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
			score=6666666
			return score

	kleuren = []
	kleuren.append(red)
	kleuren.append(green)
	kleuren.append(blue)
	kleuren.append(yellow)
	kleuren.append(orange)
	kleuren.append(purple)
	kleuren.append(grey)
	# print(kleuren)
	bubbleSort(kleuren)
	# print(kleuren)
	score += kleuren[0]*19
	score += kleuren[1]*20
	score += kleuren[2]*21
	score += kleuren[3]*23
	score += kleuren[4]*36
	score += kleuren[5]*37
	score += kleuren[6]*38
	return score

def scoreCounter3(G, colormap):
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
			score=6666666
			return score

	kleuren = []
	kleuren.append(red)
	kleuren.append(green)
	kleuren.append(blue)
	kleuren.append(yellow)
	kleuren.append(orange)
	kleuren.append(purple)
	kleuren.append(grey)
	# print(kleuren)
	bubbleSort(kleuren)
	# print(kleuren)
	score += kleuren[0]*16
	score += kleuren[1]*17
	score += kleuren[2]*31
	score += kleuren[3]*33
	score += kleuren[4]*36
	score += kleuren[5]*56
	score += kleuren[6]*57
	return score

def scoreCounter4(G, colormap):
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
			score=6666666
			return score

	kleuren = []
	kleuren.append(red)
	kleuren.append(green)
	kleuren.append(blue)
	kleuren.append(yellow)
	kleuren.append(orange)
	kleuren.append(purple)
	kleuren.append(grey)
	# print(kleuren)
	bubbleSort(kleuren)
	# print(kleuren)
	score += kleuren[0]*3
	score += kleuren[1]*34
	score += kleuren[2]*36
	score += kleuren[3]*39
	score += kleuren[4]*41
	score += kleuren[5]*43
	score += kleuren[6]*58
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

	# als er kleuren beschibkaar zijn, voeg een kleur toe
	if colorsAvailable != []:
		# kleur een node in van een specifieke kleur
		G.nodes[node]['color'] = random.choice(colorsAvailable)
	# als er geen kleur beschikbaar is, maak de node zwart
	else:
		G.nodes[node]['color'] = "black"


if __name__ == '__main__':
	main()