# Excellent video to understand insertion sort: 
# http://courses.cs.vt.edu/csonline/Algorithms/Lessons/InsertionCardSort/insertioncardsort.html


def swap(i,j,arr):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp

def insertion_sort(arr):
	last = len(arr)
	sorted_until = 1
	while sorted_until < last:
		for i in range (sorted_until, 0, -1):
			if arr[i] < arr[i-1]:
				swap(i, i-1, arr)
		sorted_until += 1
	return arr