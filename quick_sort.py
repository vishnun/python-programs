def swap(arr, i, j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp


def partition(arr, low, high):
	pivot = arr[high]
	center_index = low
	for i in range(low, high):
		if arr[i] < pivot:
			swap(arr, i, center_index)
			center_index += 1

	swap(arr, center_index, high)
	return center_index


def q_sort(arr, low, high):
	if low < high:
		p = partition(arr, low, high)
		q_sort(arr, low, p - 1)
		q_sort(arr, p + 1, high)


def quick_sort(arr):
	q_sort(arr, 0, len(arr) - 1)
	return arr
