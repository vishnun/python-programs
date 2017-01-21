def linear_search (arr, query):
	found = False
	for index, num in enumerate(arr):
		if (num == query):
			print "{} found at position {}".format(num, index)
			found = True
			break

	if not found:
		print "Not found\narr: " 
		print arr
	return found

# query = get_input()
# linear_search(arr, query)