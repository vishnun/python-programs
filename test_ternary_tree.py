import time

import ternary_tree as t_tree

# Test Tree:
#    			7 <- root
#    		  / 7  \
#  			 4 	7 	9
#	 	   / 4 \  / 9 \
#		  2    5  8   10


def test_insert():
    tree = t_tree.TernaryTree()
    tree.insert(7)
    tree.insert(9)
    tree.insert(4)
    tree.insert(7)

    first_left = tree.root.left
    first_right = tree.root.right
    first_middle = tree.root.middle

    assert tree.root.data == 7
    assert first_left.data == 4
    assert first_right.data == 9
    assert first_middle.data == 7

    tree.insert(4)
    tree.insert(2)
    tree.insert(4)
    tree.insert(10)
    tree.insert(9)
    tree.insert(8)
    tree.insert(5)
    tree.insert(7)

    assert first_left.left.data == 2
    assert first_left.right.data == 5
    assert first_left.middle.data == 4
    assert first_right.left.data == 8
    assert first_right.right.data == 10
    assert first_right.middle.data == 9
    assert first_middle.middle.data == 7