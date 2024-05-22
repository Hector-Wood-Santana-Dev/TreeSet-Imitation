"""Implementing a red-black tree on python."""


class TreeNode:
    """Class representing a tree node."""

    def __init__(self, key, color, parent=None, left=None, right=None):
        """Initialize the node."""
        self.key = key
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right


class TreeSet:
    """Class representing a tree set."""

    def __init__(self):
        """Initialize the tree set."""
        self.TNULL = TreeNode(None, "black")
        self.TNULL.left = self.TNULL
        self.TNULL.right = self.TNULL
        self.root = self.TNULL

    def __rotate_left(self, x):
        """Rotate the left side of the tree."""
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def __rotate_right(self, x):
        """Rotate the right side of the tree."""
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def __fix_insert(self, k):
        """Fix insertion order."""
        while k.parent.color == "red":
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == "red":
                    u.color = "black"
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.__rotate_right(k)
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    self.__rotate_left(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == "red":
                    u.color = "black"
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.__rotate_left(k)
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    self.__rotate_right(k.parent.parent)
            if k == self.root:
                break
        self.root.color = "black"

    def add(self, key):
        """Verify if the key is in the tree."""
        if self.contains(key):
            return False
        """Add a node to the tree."""
        node = TreeNode(key, "red")
        node.left = self.TNULL
        node.right = self.TNULL
        node.parent = None

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        if node.parent is None:
            node.color = "black"
            return True

        if node.parent.parent is None:
            return True

        self.__fix_insert(node)
        return True

    def __transplant(self, u, v):
        """Transplant the tree."""
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def __fix_delete(self, x):
        """Fix delete."""
        while x != self.root and x.color == "black":
            if x == x.parent.left:
                s = x.parent.right
                if s.color == "red":
                    s.color = "black"
                    x.parent.color = "red"
                    self.__rotate_left(x.parent)
                    s = x.parent.right
                if s.left.color == "black" and s.right.color == "black":
                    s.color = "red"
                    x = x.parent
                else:
                    if s.right.color == "black":
                        s.left.color = "black"
                        s.color = "red"
                        self.__rotate_right(s)
                        s = x.parent.right
                    s.color = x.parent.color
                    x.parent.color = "black"
                    s.right.color = "black"
                    self.__rotate_left(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == "red":
                    s.color = "black"
                    x.parent.color = "red"
                    self.__rotate_right(x.parent)
                    s = x.parent.left
                if s.right.color == "black" and s.left.color == "black":
                    s.color = "red"
                    x = x.parent
                else:
                    if s.left.color == "black":
                        s.right.color = "black"
                        s.color = "red"
                        self.__rotate_left(s)
                        s = x.parent.left
                    s.color = x.parent.color
                    x.parent.color = "black"
                    s.left.color = "black"
                    self.__rotate_right(x.parent)
                    x = self.root
        x.color = "black"

    def __delete_node_helper(self, node, key):
        """Delete a node from the tree."""
        z = self.TNULL
        while node != self.TNULL:
            if node.key == key:
                z = node

            if node.key <= key:
                node = node.right
            else:
                node = node.left

        if z == self.TNULL:
            return False

        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self.__transplant(z, z.right)
        elif z.right == self.TNULL:
            x = z.left
            self.__transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.__transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.__transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == "black":
            self.__fix_delete(x)
        return True

    def remove(self, key):
        """Remove a node from the tree."""
        return self.__delete_node_helper(self.root, key)

    def minimum(self, node):
        """Return the minimum node in the tree."""
        while node.left != self.TNULL:
            node = node.left
        return node

    def maximum(self, node):
        """Return the maximum node in the tree."""
        while node.right != self.TNULL:
            node = node.right
        return node

    def search_tree_helper(self, node, key):
        """Search for a node in the tree."""
        if node == self.TNULL or key == node.key:
            return node

        if key < node.key:
            return self.search_tree_helper(node.left, key)
        return self.search_tree_helper(node.right, key)

    def contains(self, key):
        """Verify if the key is in the tree."""
        node = self.search_tree_helper(self.root, key)
        return node != self.TNULL

    def __iter__(self):
        """Iterate over the tree."""
        stack = []
        node = self.root
        while stack or node != self.TNULL:
            while node != self.TNULL:
                stack.append(node)
                node = node.left
            node = stack.pop()
            yield node.key
            node = node.right

    def descendingIterator(self):
        """Returns an iterator over the elements in this set in descending order."""
        stack = []
        node = self.root
        while stack or node != self.TNULL:
            while node != self.TNULL:
                stack.append(node)
                node = node.right
            node = stack.pop()
            yield node.key
            node = node.left

    def first(self):
        """Return the first node in the tree."""
        node = self.minimum(self.root)
        if node == self.TNULL:
            return None
        return node.key

    def last(self):
        """Return the last node in the tree."""
        node = self.maximum(self.root)
        return node.key if node != self.TNULL else None

    def size(self):
        """Return the size of the tree."""
        return sum(1 for _ in self)

    def clear(self):
        """Clear the entire tree."""
        self.root = self.TNULL

    def addAll(self, collection):
        """Add all elements in the collection to the tree."""
        added = False
        for item in collection:
            if self.add(item):
                added = True
        return added

    def ceiling(self, e):
        """Ceiling an element in the tree."""
        node = self.root
        ceiling = None
        while node != self.TNULL:
            if e < node.key:
                ceiling = node.key
                node = node.left
            elif e > node.key:
                node = node.right
            else:
                return node.key
        return ceiling

    def floor(self, e):
        """Floor an element in the tree."""
        node = self.root
        floor = None
        while node != self.TNULL:
            if e > node.key:
                floor = node.key
                node = node.right
            elif e < node.key:
                node = node.left
            else:
                return node.key
        return floor

    def higher(self, e):
        """Higher an element in the tree."""
        node = self.root
        higher = None
        while node != self.TNULL:
            if e < node.key:
                higher = node.key
                node = node.left
            else:
                node = node.right
        return higher

    def lower(self, e):
        """Lower an element in the tree."""
        node = self.root
        lower = None
        while node != self.TNULL:
            if e > node.key:
                lower = node.key
                node = node.right
            else:
                node = node.left
        return lower

    def pollFirst(self):
        """Return the first node in the tree."""
        node = self.minimum(self.root)
        if node == self.TNULL:
            return None
        key = node.key
        self.remove(node.key)
        return key

    def pollLast(self):
        """Return the last node in the tree."""
        node = self.maximum(self.root)
        if node == self.TNULL:
            return None
        key = node.key
        self.remove(node.key)
        return key

    def isEmpty(self):
        """Return True if the tree is empty."""
        return self.root == self.TNULL

    def clone(self):
        """Return a clone of the tree."""
        new_tree = TreeSet()
        for key in self:
            new_tree.add(key)
        return new_tree
