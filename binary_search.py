def binary_search(list, query):
	first = 0;
	last = len(list)
	found = False
	while first < last:
		mid = (first+last) / 2
		print mid
		if list[mid] == query:
			found = True
			break
		elif list[mid] < query:
			first = mid+1
		else:
			last = mid-1

	if not found:
		print "Couldn't find {} in the list {}".format(query, list)
	else:
		print "Found {} in the list at position {}".format(query, mid)

	return found
