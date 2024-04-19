class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.color = "RED"

class TreeSet:
    def __init__(self):
        self.root = None

    def insert(self, value):
