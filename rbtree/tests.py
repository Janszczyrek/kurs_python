import unittest
import random
from rbtree import RBtree


def test_rb_properties(tree):
    # 2. Root node is black
    if tree.root.color is not RBtree.RBnode.BLACK:
        print("property 2 violation")
        return False
    # 4. All paths have the same black count
    if tree.black_height == -1:
        print("property 4 violation")
        return False
    return test_rb_properties_helper(tree, tree.root)


def test_rb_properties_helper(
        tree,
        node,
        current_black_count=0,
        min_black_count=None):
    # Base case
    if node is None:
        return True

    # 1. Every node is either red or black
    if node.color not in [RBtree.RBnode.BLACK, RBtree.RBnode.RED]:
        print("property 1 violation")
        return False

    # 3. Red nodes have black children
    if node.color is RBtree.RBnode.RED and (
        (node.leftChild and node.leftChild.color is RBtree.RBnode.RED)
        or (node.rightChild and node.rightChild.color is RBtree.RBnode.RED)
    ):
        print("property 3 violation")
        return False

    left_valid = test_rb_properties_helper(
        tree, node.leftChild, current_black_count, min_black_count
    )
    right_valid = test_rb_properties_helper(
        tree, node.rightChild, current_black_count, min_black_count
    )

    return left_valid and right_valid


class TestRBtree(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # wizualizacja stworzonego drzewa znajduje się w pliku
        # drzewo_test_1.jpg i została stworzona w narzędziu: 
        # https://www.cs.usfca.edu/~galles/visualization/RedBlack.html
        cls.tree = RBtree()
        cls.tree.insert(1, 19, 0, 5, 2, 2, 1, 10)
        cls.tree.insert(142)
        cls.tree.insert(18)
        cls.tree.tree_print()

    def test_random_insert(self):
        tree = RBtree()
        [tree.insert(random.randint(-100, 100)) for x in range(1000)]
        self.assertEqual(test_rb_properties(tree), True)

    def test_properties(self):
        # Sprawdzenie czy funkcja testująca właściwości poprawnie identyfikuje
        # błędy.
        self.assertEqual(test_rb_properties(self.tree), True)
        self.tree.root.leftChild.color = 2
        self.assertEqual(test_rb_properties(self.tree), False)
        self.tree.root.leftChild.color = 1

        self.assertEqual(test_rb_properties(self.tree), True)
        self.tree.root.color = 2
        self.assertEqual(test_rb_properties(self.tree), False)
        self.tree.root.color = 0

        self.assertEqual(test_rb_properties(self.tree), True)
        self.tree.root.leftChild.rightChild.leftChild.rightChild = RBtree.RBnode(
            1, color=RBtree.RBnode.RED)
        self.assertEqual(test_rb_properties(self.tree), False)
        self.tree.root.leftChild.rightChild.leftChild.rightChild = None
        self.assertEqual(test_rb_properties(self.tree), True)

        self.assertEqual(test_rb_properties(self.tree), True)
        self.tree.root.leftChild.leftChild.color = 1
        self.assertEqual(test_rb_properties(self.tree), False)
        self.tree.root.leftChild.leftChild.color = 0
        self.assertEqual(test_rb_properties(self.tree), True)

    def test_search(self):
        self.assertEqual(self.tree.search(5), self.tree.root)
        self.assertEqual(self.tree.search(-1), None)
        self.assertEqual(
            self.tree.search(142),
            self.tree.root.rightChild.rightChild)
        self.assertEqual(
            self.tree.search(0),
            self.tree.root.leftChild.leftChild)
        self.assertEqual(self.tree.search(18),
                         self.tree.root.rightChild.leftChild.rightChild)
        self.assertEqual(self.tree.search(19), self.tree.root.rightChild)
        self.assertEqual(
            self.tree.search(2),
            self.tree.root.leftChild.rightChild)

    def test_clear(self):
        tree = RBtree()
        [tree.insert(random.randint(-100, 100)) for x in range(10)]
        tree.clear()
        self.assertEqual(tree.root, None)
        self.assertEqual(tree.redRedConflict, False)
        self.assertEqual(tree.ll, False)
        self.assertEqual(tree.lr, False)
        self.assertEqual(tree.rr, False)
        self.assertEqual(tree.rl, False)
        tree.insert(1)
        tree.insert(2)
        tree.insert(3)
        self.assertEqual(tree.root.data, 2)

    def test_traversal(self):
        self.assertEqual([x.data for x in 
        self.tree.preorder_traverse(self.tree.root)],[5,1,0,2,1,2,19,10,18,142])

        self.assertEqual([x.data for x in 
        self.tree.inorder_traverse(self.tree.root)],[0,1,1,2,2,5,10,18,19,142])

        self.assertEqual([x.data for x in 
        self.tree.postorder_traverse(self.tree.root)],[0,1,2,2,1,18,10,142,19,5])

unittest.main()
