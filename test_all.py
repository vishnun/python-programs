import time
import linear_search as ls
import binary_search as bs
import bubble_sort as bbs

def test_linear_search():
	assert ls.linear_search([2,3,4], 3) == True
	assert ls.linear_search([2,3,4], 6) == False

def test_binary_search():
	assert bs.binary_search([2,3,4,6,8,9], 3) == True
	assert bs.binary_search([2,3,4,6,8,9], 9) == True
	assert bs.binary_search([2,3,4,6,8,9], 6) == True
	assert bs.binary_search([2,3,4,6,8,9], 19) == False


def test_bubble_sort():
	assert bbs.bubble_sort([1,2,3,4,5]) == [1,2,3,4,5]
	assert bbs.bubble_sort([1,6,4,3,7,6,5]) == [1,3,4,5,6,6,7]