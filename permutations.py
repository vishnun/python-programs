
def swap(arr, i,j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp


def perm(A, start, end):
	if start == end:
		print A
	else:
		for i in range(start, end+1):
			swap(A, i, start)
			perm(A, start+1, end)
			swap(A, i, start)




arr = ['a','b','c']
perm(arr, 0, len(arr)-1)