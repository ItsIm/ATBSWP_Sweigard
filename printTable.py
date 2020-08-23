# Форматированный вывод строк

tableData = [['apples', 'oranges', 'cherries', 'banana'],
			 ['Alice', 'Bob', 'Carol', 'David'],
			 ['dogs', 'cats', 'moose', 'goose']]

def print_table(listPrint, listTwo, biggestInList):
	length = listTwo[biggestInList]
	for i in range(len(listPrint)):
		print(''.join(listPrint[i]).rjust(length))

def calc_for_more(list):
	colWidthTwo = []

	for i in range(len(list)):
		colWidth = []
		for j in range(len(list[i])):
			colWidth.append(len(list[i][j]))
		colWidthTwo.append(sum(colWidth))
	return colWidthTwo


def search_for_more(list):
	big = 0
	for i in range(len(list)):
		if list[i] > list[i-1]:
			big = i
	return big


colWidth = calc_for_more(tableData)
biggestInList = search_for_more(colWidth)
print_table(tableData, colWidth, biggestInList)
