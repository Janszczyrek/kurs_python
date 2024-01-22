from rbtree import RBtree

tree = RBtree()

tree.insert(10)
tree.insert(20)
tree.insert(5)
tree.insert(55)

print("***preorder***")
tree.preorder_print()

print("***inorder***")
tree.inorder_print()

print("***postorder***")
tree.postorder_print()

tree.tree_print()

node5 = tree.search(5)
print(node5)

print(tree.is_empty)
tree.clear()
print(tree.is_empty)