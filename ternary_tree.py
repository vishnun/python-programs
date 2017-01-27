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
		""" Insert the node to the left of the node. """
		if root.left is None:
			root.left = node
		else:
			self.__insert_node(root.left, node)

	def __insert_to_right(self, node, root):
		""" Insert the node to the right of the node. """
		if root.right is None:
			root.right = node
		else:
			self.__insert_node(root.right, node)

	def __insert_node(self, root, node):
		""" Recursively insert the node at it's correct location. """
		if node.data == root.data:
			while root.middle is not None:
				root = root.middle
			root.middle = node
		elif node.data < root.data:
			self.__insert_to_left(node, root)
		elif node.data > root.data:
			self.__insert_to_right(node, root)

	def __find_smallest(self, node, parent):
		"""Finds the smallest element in the subtree with node as the root and
		returns the parent of as well of the smallest node."""
		while node.left is not None:
			parent = node
			node = node.left
		return node, parent

	def __is_leaf_node(self, node):
		"""Checks if the node is a leaf node with no children at all."""
		return (node.left is None) and (node.right is None) and (node.middle is None)

	def __has_left_or_right_child(self, node):
		"""Check if the child has only left or a right child."""
		return (node.left is None) or (node.right is None)

	def __delete_if_one_child(self, node):
		"""Delete the node when it has only one child."""
		if node.left is not None:
			node.data = node.left.data
			left = node.left
			node.left = None
			del left
		else:
			node.data = node.right.data
			right = node.right
			node.right = None
			del right

	def __has_middle_child(self, node):
		"""Check if a node has a middle child"""
		return node.middle is not None

	def __delete_if_left_and_right_children(self, node):
		"""delete if a node has left and a right tree"""
		smallest, parent = self.__find_smallest(node.right, node)
		node.data = smallest.data
		self.__delete_node(smallest, parent)

	def __delete_leaf_node(self, node, parent):
		"""Delete the leaf node."""
		if parent.left is node:
			parent.left = None
		elif parent.right is node:
			parent.right = None
		del node

	def __delete_node(self, node, parent):
		""" Delete a node from the tree. Needs parent to keep it optimal. """
		if self.__has_middle_child(node):
			self.__delete_with_middle_child(node, parent)
		elif self.__is_leaf_node(node):
			self.__delete_leaf_node(node, parent)
		elif self.__has_left_or_right_child(node):
			self.__delete_if_one_child(node)
		else:
			self.__delete_if_left_and_right_children(node)

	def __delete_with_middle_child(self, node, parent):
		""" Delete a node that has one or more middle children."""
		while node.middle is not None:
			parent = node
			node = node.middle
		parent.middle = None
		del node

	def insert(self, data):
		""" Insert a new node at it's appropriate location in the search tree. """
		node = Node(data)
		if self.root is None:
			self.root = node
		else:
			self.__insert_node(self.root, node)

	def search(self, data):
		""" Search for a node with the query data and return (data, parent) tuple for the node found."""
		start = self.root
		parent = None
		while start is not None:
			if data == start.data:
				return start, parent
			elif data < start.data:
				parent = start
				start = start.left
			elif data > start.data:
				parent = start
				start = start.right
		return None, None

	def delete(self, data):
		""" Delete a node from the tree. """
		node, parent = self.search(data)
		self.__delete_node(node, parent)
