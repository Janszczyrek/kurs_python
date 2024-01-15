import unittest
from rbtree import RBtree

class TestRBtree(unittest.TestCase):
    def test_init(self):
        tree = RBtree()
        tree.insert(1)
        tree.preorder()
        tree.insert(19)
        tree.preorder()
        tree.insert(0)
        tree.preorder()
        tree.insert(5)
        tree.preorder()
        tree.insert(2)
        tree.preorder()
        tree.insert(2) 
        tree.preorder()
        tree.insert(1)
        tree.preorder()
        tree.insert(10)
        tree.preorder()
        tree.insert(142)
        tree.preorder()
        tree.insert(18)
        tree.preorder()
        print(tree.root)

unittest.main()