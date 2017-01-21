
def swap(i,j,list):
	temp = list[i]
	list[i] = list[j]
	list[j] = temp


def bubble_sort(list):
	last = len(list)
	sorted = False
	while not sorted:
		sorted = True
		for i in range(last-1):
			if (list[i] > list[i+1]):
				swap(i,i+1,list)
				sorted = False

	return list