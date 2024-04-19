"""Implementation of the tree set class in python."""
class Node:
    """Class representing a node in the tree."""
    def __init__(self, value):
        """Initialize the node with the given value."""
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.color = "RED"

class TreeSet:
    """Class representing a tree set."""
    def __init__(self):
        """Initialize the tree set."""
        self.root = None
        self.type =

    def is_sequence(param):
        """Method to check if a value is a sequence."""
        return isinstance(param, (list, tuple, set, str))

    def insert(self, value):
        """Method to insert a value into the tree."""
        if not isinstance(value, self.type):
            raise TypeError("The element must be of type '{}'".format(self.type))
    def insertAll(self, collection):
        """Method to insert a collection into the tree."""
        for element in collection:
            if not isinstance(element, self.type):
                raise TypeError("One or more elements must be of type '{}'".format(self.type))
            self.insert(element)
    def is_sequence(param):
        """Method to check if a value is a sequence."""
        return isinstance(param, (list, tuple, set, str))

