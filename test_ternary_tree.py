# Test Tree:
#    			7 <- root
#    		  / 7  \
#  			 4 	7 	9
#	 	   / 4 \     \
#		  2    5      10


import ternary_tree as t_tree


def _insert_nodes(tree):
	""" Helper method to create above test tree structure."""
	tree.insert(7)
	tree.insert(9)
	tree.insert(4)
	tree.insert(7)
	tree.insert(4)
	tree.insert(2)
	tree.insert(10)
	tree.insert(5)
	tree.insert(7)


def test_insert():
	""" Tests inserting of nodes. Referes the test tree above and checks for the structure. """
	tree = t_tree.TernaryTree()

	_insert_nodes(tree)

	first_left = tree.root.left
	first_right = tree.root.right
	first_middle = tree.root.middle

	assert tree.root.data == 7
	assert first_left.data == 4
	assert first_right.data == 9
	assert first_middle.data == 7
	assert first_left.left.data == 2
	assert first_left.right.data == 5
	assert first_left.middle.data == 4
	assert first_right.right.data == 10
	assert first_middle.middle.data == 7


def test_search():
	""" Tests searching of a node in the tree. If found, it returns node and it's parent."""
	tree = t_tree.TernaryTree()
	_insert_nodes(tree)

	assert tree.search(10)[0].data == 10
	assert type(tree.search(10)[0]) == t_tree.Node
	assert tree.search(9)[0].data == 9
	assert type(tree.search(9)[0]) == t_tree.Node
	assert tree.search(4)[0].data == 4
	assert type(tree.search(4)[0]) == t_tree.Node
	assert tree.search(1)[0] is None


def test_delete_leaf():
	""" Tests deletion when node has no children """
	tree = t_tree.TernaryTree()
	_insert_nodes(tree)
	assert tree.search(5)[0] is not None
	tree.delete(5)
	assert tree.search(5)[0] is None


def test_delete_with_one_child():
	""" Tests deletion when a node has one child"""
	tree = t_tree.TernaryTree()
	_insert_nodes(tree)
	assert tree.search(9)[0] is not None
	tree.delete(9)
	assert tree.search(9)[0] is None


def test_delete_with_multiple_children():
	""" Tests deletion of all cases with more than 1 child """
	tree = t_tree.TernaryTree()
	_insert_nodes(tree)
	# When has middle child
	assert tree.search(4)[0] is not None
	tree.delete(4)
	assert tree.search(4)[0] is not None
	# when middle child is not present
	tree.delete(4)
	assert tree.search(4)[0] is None
