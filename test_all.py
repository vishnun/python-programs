import time

import linear_search as ls
import binary_search as bs
import bubble_sort as bbs
import insertion_sort as ins
import quick_sort as qs
import simple_stack as ss
import permutations as p


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

def test_insertion_sort():
	assert ins.insertion_sort([1,2,3,4,5]) == [1,2,3,4,5]
	assert ins.insertion_sort([4,3,6,1]) == [1,3,4,6]
	assert ins.insertion_sort([1,6,4,3,7,6,5]) == [1,3,4,5,6,6,7]

def test_quick_sort():
	assert qs.quick_sort([1,2,3,4,5]) == [1,2,3,4,5]
	assert qs.quick_sort([4,3,6,1,9,2,8]) == [1, 2, 3, 4, 6, 8, 9]
	assert qs.quick_sort([1,6,4,3,7,6,5]) == [1,3,4,5,6,6,7]


def test_simple_stack():
	ss.push("a")
	ss.push("x")
	assert ss.peek() == "x"
	assert ss.pop() == "x"
	assert ss.peek() == "a"


def test_permutations():
	result = [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]
	assert p.get_permutations([1,2,3]) == result