
def swap(i,j,list):
	temp = list[i]
	list[i] = list[j]
	list[j] = temp


def bubble_sort(list):
	last = len(list)

	for i in range(last):
		for j in range(i+1,last):
			if (list[i] > list[j]):
				swap(i,j,list)
				swapped = True

	return list