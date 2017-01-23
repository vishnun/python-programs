
def swap(arr, i,j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp


def perm(A, start, end, result):
	if start == end:
		result.append(A)
	else:
		for i in range(start, end+1):
			swap(A, i, start)
			perm(A, start+1, end, result)
			swap(A, i, start)


def get_permutations(arr):
	result = []
	perm(arr,0,len(arr) -1, result)
	return result