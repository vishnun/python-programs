def linear_search (list, query):
	found = False
	for index, num in enumerate(list):
		if (num == query):
			print "{} found at position {}".format(num, index)
			found = True
			break

	if not found:
		print "Not found\nList: " 
		print list
	return found

# query = get_input()
# linear_search(list, query)