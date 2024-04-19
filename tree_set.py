"""Implementation of the tree set class in python."""


class Node:
    """Class representing a node in the tree."""
    def __init__(self, value, color):
        """Initialize the node with the given value."""
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.color = color


class TreeSet:
    """Class representing a tree set."""
    def __init__(self):
        """Initialize the tree set."""
        self.root = None
        self.type = int

    @staticmethod
    def is_sequence(param):
        """Method to check if a value is a sequence."""
        return isinstance(param, (list, tuple, set, str))

    def insert(self, value):
        """Method to insert a value into the tree."""
        if not isinstance(value, self.type):
            raise TypeError("The element must be of type '{}'".format(self.type))

    def _insert_recursive(self, node, value):
        """Method to insert a value into the tree, first compare left side and then right side."""
        if node is None:
            return Node(value, "Red")
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        return self._balance(node)

    def insert_all(self, collection):
        """Method to insert a collection into the tree."""
        if self.is_sequence(collection):
            for element in collection:
                if not isinstance(element, self.type):
                    raise TypeError("One or more elements must be of type '{}'".format(self.type))
                self.insert(element)
        else:
            raise ValueError("Its not a collection")

    def _balance(self, node):
        # Caso 1: The node is the root
        if node.parent is None:
            node.color = "BLACK"
            return node

        # Caso 2: The parent of node is the root
        if node.parent.color == "BLACK":
            return node

        # Caso 3: The parent and uncle are reds
        if self._is_red(node.uncle):
            node.parent.color = "BLACK"
            node.uncle.color = "BLACK"
            node.grandparent.color = "RED"
            return self._balance(node.grandparent)

    @staticmethod
    def _is_red(node):
        return node is not None and node.color == "RED"

    def _left_rotate(self, node):
        pivot = node.right
        node.right = pivot.left
        if pivot.left is not None:
            pivot.left.parent = node
        pivot.parent = node.parent
        if node.parent is None:
            self.root = pivot
        elif node.is_left_child():
            node.parent.left = pivot
        else:
            node.parent.right = pivot
        pivot.left = node
        node.parent = pivot

    def _right_rotate(self, node):
        pivot = node.left
        node.left = pivot.right
        if pivot.right is not None:
            pivot.right.parent = node
        pivot.parent = node.parent
        if node.parent is None:
            self.root = pivot
        elif node.is_right_child():
            node.parent.right = pivot
        else:
            node.parent.left = pivot
        pivot.right = node
        node.parent = pivot
