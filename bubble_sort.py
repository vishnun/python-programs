
def swap(i,j,arr):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp


def bubble_sort(arr):
	last = len(arr)
	sorted = False
	while not sorted:
		sorted = True
		for i in range(last-1):
			if (arr[i] > arr[i+1]):
				swap(i,i+1,arr)
				sorted = False

	return arr