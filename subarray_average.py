# Break an array into maximum number of sub-arrays such that their averages are same
import math


def find_subarray_with_same_average(Arr):
	average = sum(Arr) / len(Arr)
	t_sum = 0
	subarrays = []
	subarray = []
	for item in Arr:
		t_sum += item
		subarray.append(item)
		if (t_sum / len(subarray)) == average:
			subarrays.append(subarray)
			subarray = []
			t_sum = 0

	return subarrays
