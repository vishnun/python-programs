def binary_search(arr, query):
	first = 0;
	last = len(arr)
	found = False
	while first < last:
		mid = (first+last) / 2
		print mid
		if arr[mid] == query:
			found = True
			break
		elif arr[mid] < query:
			first = mid+1
		else:
			last = mid-1

	if not found:
		print "Couldn't find {} in the arr {}".format(query, arr)
	else:
		print "Found {} in the arr at position {}".format(query, mid)

	return found
