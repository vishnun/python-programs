# Excellent video to understand insertion sort: 
# http://courses.cs.vt.edu/csonline/Algorithms/Lessons/InsertionCardSort/insertioncardsort.html


def swap(i,j,list):
	temp = list[i]
	list[i] = list[j]
	list[j] = temp

def insertion_sort(list):
	last = len(list)
	sorted_until = 1
	while sorted_until < last:
		for i in range (sorted_until, 0, -1):
			if list[i] < list[i-1]:
				swap(i, i-1, list)
		sorted_until += 1
	return list