import unittest

from tree_set import TreeSet


class TestTreeSetComplexWithRotationsandColorations(unittest.TestCase):
    def setUp(self):
        self.tree = TreeSet()
        elementos = [10, 85, 15, 70, 20, 60, 30, 50, 65, 80, 90, 40, 5, 55]
        for e in elementos:
            self.tree.add(e)

    def test01_elements(self):
        """Test that the elements in the tree are as expected."""
        self.assertEqual(list(self.tree), [5, 10, 15, 20, 30, 40, 50, 55, 60, 65, 70, 80, 85, 90],
                         'The iterator must be [5, 10, 15, 20, 30, 40, 50, 55, 60, 65, 70, 80, 85, 90]')

    def test02_first(self):
        """Test that the first element in the tree is as expected."""
        self.assertEqual(self.tree.first(), 5, "Must return 5")

    def test03_last(self):
        """Test that the last element in the tree is as expected."""
        self.assertEqual(self.tree.last(), 90, "Must return 90")

    def test04_size(self):
        """Test that the size of the tree is as expected."""
        self.assertEqual(self.tree.size(), 14, "The size must be 14")

    def test05_ceiling(self):
        """Test that the ceiling of the tree is as expected."""
        self.assertEqual(self.tree.ceiling(56), 60, "Must return 60")

    def test06_floor(self):
        """Test that the floor of the tree is as expected."""
        self.assertEqual(self.tree.floor(56), 55, "Must return 55")

    def test07_higher(self):
        """Test that the higher element in the tree is as expected."""
        self.assertEqual(self.tree.higher(70), 80, "Must return 80")

    def test08_lower(self):
        """Test that the lower element in the tree is as expected."""
        self.assertEqual(self.tree.lower(70), 65, "Must return 65")

    def test09_remove(self):
        """Test that the remove element in the tree is as expected."""
        self.assertTrue(self.tree.remove(10), "Must return True when deleting 10")
        self.assertFalse(self.tree.contains(10), "Should not contain 10 after removal")
        self.assertEqual(list(self.tree), [5, 15, 20, 30, 40, 50, 55, 60, 65, 70, 80, 85, 90],
                         'The iterator must return [5, 15, 20, 30, 40, 50, 55, 60, 65, 70, 80, 85, 90]')


if __name__ == '__main__':
    unittest.main()
