from unittest import TestCase
import subarray_average as sub_avg


class Test_Find_subarray_with_same_average(TestCase):
	def test_find_subarray_with_same_average(self):
		assert sub_avg.find_subarray_with_same_average([1, 5, 7, 2, 0]) == [[1, 5], [7, 2, 0]]
		assert sub_avg.find_subarray_with_same_average([4, 6, 2, 4, 8, 0, 6, 2]) == [[4], [6, 2], [4], [8, 0], [6, 2]]
