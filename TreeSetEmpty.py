import unittest

from tree_set import TreeSet


class TestTreeSetEmpty(unittest.TestCase):
    def setUp(self):
        self.tree = TreeSet()

    def test01_isEmpty(self):
        """Test whether an empty tree is empty."""
        self.assertTrue(self.tree.isEmpty(), "The TreeSet must be empty")

    def test02_size(self):
        """Test whether an empty tree is full."""
        self.assertEqual(self.tree.size(), 0, "The size must be zero")

    def test03_first(self):
        """Test whether an empty tree is empty."""
        self.assertIsNone(self.tree.first(), "Must return None")

    def test04_last(self):
        """Test whether an empty tree is empty."""
        self.assertIsNone(self.tree.last(), "Must return None")

    def test05_pollFirst(self):
        """Test whether an empty tree is empty."""
        self.assertIsNone(self.tree.pollFirst(), "Must return None")

    def test06_pollLast(self):
        """Test whether an empty tree is empty."""
        self.assertIsNone(self.tree.pollLast(), "Must return None")

    def test07_contains(self):
        """Test whether an empty tree is empty."""
        self.assertFalse(self.tree.contains(1), "Must return False")

    def test08_iterator(self):
        """Test whether an empty tree is empty."""
        self.assertEqual(list(self.tree), [], "The tree must be empty")


if __name__ == '__main__':
    unittest.main()
