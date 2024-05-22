import unittest

from tree_set import TreeSet


class TestTreeSetComplexWithRotations(unittest.TestCase):
    def setUp(self):
        self.tree = TreeSet()
        elementos = [30, 20, 40, 10, 25, 35, 50]
        for e in elementos:
            self.tree.add(e)

    def test01_elements(self):
        """Test that the elements are correctly added."""
        self.assertEqual(list(self.tree), [10, 20, 25, 30, 35, 40, 50], "The iter must be[10, 20, 25, 30, 35, 40, 50]")

    def test02_first(self):
        """Test that the first element of the tree is correctly added."""
        self.assertEqual(self.tree.first(), 10, "Must return 10")

    def test03_last(self):
        """Test that the last element of the tree is correctly added."""
        self.assertEqual(self.tree.last(), 50, "Must return 50")

    def test04_size(self):
        """Test that the size of the tree is correctly added."""
        self.assertEqual(self.tree.size(), 7, "The size must be 7")

    def test05_ceiling(self):
        """Test that the ceiling of the tree is correctly added."""
        self.assertEqual(self.tree.ceiling(26), 30, "Must return 30")

    def test06_floor(self):
        """Test that the floor of the tree is correctly added."""
        self.assertEqual(self.tree.floor(26), 25, "Must return 25")

    def test07_higher(self):
        """Test that the higher element of the tree is correctly added."""
        self.assertEqual(self.tree.higher(40), 50, "Must return 50")

    def test08_lower(self):
        """Test that the lower element of the tree is correctly added."""
        self.assertEqual(self.tree.lower(40), 35, "Must return 35")


if __name__ == '__main__':
    unittest.main()
