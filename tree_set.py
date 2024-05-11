class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.color = "RED"

    def is_left_child(self):
        return self == self.parent.left if self.parent else False

    def flip_color(self):
        self.color = "BLACK" if self.color == "RED" else "RED"


class TreeSet:
    def __init__(self):
        self.root = None

    def insert(self, data):
        node = Node(data)
        self.root = self.insert(self.root, node)
        self.recolor_and_rotate(node)

    def insert_especific(self, node, node_to_insert):
        if self.root is None:
            return node_to_insert
        if node_to_insert.data < node.data:
            self.insert(node.left, node_to_insert)
            node.left.parent = node
        elif node_to_insert.data > node.data:
            node.right = self.insert(node.right, node_to_insert)
            node.right.parent = node
        return node

    def recolor_and_rotate(self, node):
        parent = node.parent
        if node != self.root and parent.color == "RED":
            grand_parent = parent.parent
            uncle = parent.left_child if parent.is_left_child() else grand_parent.right_child
            if uncle is not None and uncle.color == "RED":  # Recoloring
                self.handle_recoloring(parent, uncle, grand_parent)
            elif parent.is_left_child():  # Left-Left or Left-Right situation
                self.handle_left_situations(node, parent, grand_parent)
            elif not parent.is_left_child():  # Right-Right or Right-Left situation
                self.handle_right_situations(node, parent, grand_parent)
        self.root.color = "BLACK"  # Color the root node black

    def handle_right_situations(self, node, parent, grand_parent):
        if node.is_left_child():
            self.rotate_right(parent)
        parent.flip_color()
        grand_parent.flip_color()
        self.rotate_left(grand_parent)
        self.recolor_and_rotate(grand_parent if node.is_left_child() else parent)

    def handle_left_situations(self, node, parent, grand_parent):
        if not node.is_left_child():
            self.rotate_left(parent)
        parent.flip_color()
        grand_parent.flip_color()
        self.rotate_right(grand_parent)
        self.recolor_and_rotate(parent if node.is_left_child() else grand_parent)

    def handle_recoloring(self, parent, uncle, grand_parent):
        uncle.flip_color()
        parent.flip_color()
        grand_parent.flip_color()
        self.recolor_and_rotate(grand_parent)

    def rotate_right(self, node):
        left_node = node.left_child
        node.left_child = left_node.right_child
        if node.left_child is not None:
            node.left_child.parent = node
        left_node.right_child = node
        left_node.parent = node.parent
        self.update_children_of_parent_node(node, left_node)
        node.parent = left_node

    def rotate_left(self, node):
        right_node = node.right_child
        node.right_child = right_node.left_child
        if node.right_child is not None:
            node.right_child.parent = node
        right_node.left_child = node
        right_node.parent = node.parent
        self.update_children_of_parent_node(node, right_node)
        node.parent = right_node

    def update_children_of_parent_node(self, node, temp_node):
        if node.parent is None:
            self.root = temp_node
        elif node.is_left_child():
            node.parent.left_child = temp_node
        else:
            node.parent.right_child = temp_node

    def traverse(self):
        self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node is not None:
            self.traverse_in_order(node.left_child)
            print(node)
            self.traverse_in_order(node.right_child)

    def get_max(self):
        if self.is_empty():
            return None
        return self._get_max(self.root)

    def _get_max(self, node):
        if node.right_child is not None:
            return self._get_max(node.right_child)
        return node.data

    def get_min(self):
        if self.is_empty():
            return None
        return self._get_min(self.root)

    def _get_min(self, node):
        if node.left_child is not None:
            return self._get_min(node.left_child)
        return node.data

    def is_empty(self):
        return self.root is None
