import unittest

from tree_set import TreeSet


class TestTreeSetSimple(unittest.TestCase):
    def setUp(self):
        self.tree = TreeSet()
        self.tree.add(5)
        self.tree.add(3)
        self.tree.add(7)

    def test01_add_duplicate(self):
        """Test that we can add a duplicate node."""
        self.assertFalse(self.tree.add(3), "Must return False when adding a duplicate")

    def test02_size(self):
        """Test that we can get size of tree."""
        self.assertEqual(self.tree.size(), 3, "The size must be 3")

    def test03_isEmpty(self):
        """Test that we can check if a tree is empty."""
        self.assertFalse(self.tree.isEmpty(), "The TreeSet should not be empty")

    def test04_first(self):
        """Test that we can find the first node in tree."""
        self.assertEqual(self.tree.first(), 3, "Must return 3")

    def test05_last(self):
        """Test that we can find the last node in tree."""
        self.assertEqual(self.tree.last(), 7, "Must return 7")

    def test06_contains(self):
        """Test that we can check if a tree contains a node."""
        self.assertTrue(self.tree.contains(5), "Must return True")

    def test07_not_contains(self):
        """Test that we can not find a node in tree."""
        self.assertFalse(self.tree.contains(10), "Must return False")

    def test08_iterator(self):
        """Test that we can iterate through a tree."""
        self.assertEqual(list(self.tree), [3, 5, 7], "The iter must return [3, 5, 7]")


if __name__ == '__main__':
    unittest.main()
