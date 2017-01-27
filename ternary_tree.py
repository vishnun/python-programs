class Node(object):
	"""Class to describe a node of a tree."""

	def __init__(self, data, left=None, right=None, middle=None):
		"""node has data, left, right and middle attributes"""
		self.left = left
		self.middle = middle
		self.right = right
		self.data = data


class TernaryTree(object):
	"""A class for a modified version of a binary search tree. One that has 3 nodes."""

	def __init__(self):
		""" A tree should have a root. Initialized it to None when the tree is created."""
		self.root = None

	def __insert_to_left(self, node, root):
		if root.left is None:
			root.left = node
		else:
			self.__insert_it(root.left, node)

	def __insert_to_right(self, node, root):
		if root.right is None:
			root.right = node
		else:
			self.__insert_it(root.right, node)

	def __insert_it(self, root, node):
		if node.data == root.data:
			while root.middle is not None:
				root = root.middle
			root.middle = node
		elif node.data < root.data:
			self.__insert_to_left(node, root)
		elif node.data > root.data:
			self.__insert_to_right(node, root)

	def insert(self, data):
		""" Insert a new node at it's appropriate location in the search tree. """
		node = Node(data)
		if self.root == None:
			self.root = node
		else:
			self.__insert_it(self.root, node)