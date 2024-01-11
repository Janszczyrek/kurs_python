import unittest
from rbtree import RBtree, RBnode

class TestRBtree(unittest.TestCase):
    def test_init(self):
        tree = RBtree()
        tree.insert(1)
        tree.insert(2)
        tree.insert(3)
        tree.inorder()

unittest.main()