class RBnode:
    def __init__(self, value, parent, leftChild, rightChild, color):
        self.value = value
        self.parent = parent
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.color = color

    def __str__(self):
        return f"Value: {self.value}, Parent: {self.parent}, lChild: {self.leftChild}, rChild: {self.rightChild}, color: {self.color}"

    def right_rotation(node):
        pivot = node.leftChild
        assert pivot is not None
        node.leftChild = pivot.rightChild
        pivot.rightChild = node
        return pivot

    def left_rotation(node):
        pivot = node.rightChild
        assert pivot is not None
        node.rightChild = pivot.leftChild
        pivot.leftChild = node
        return pivot

    def lr_rotation(node):
        assert node.leftChild is not None
        node.leftChild = RBnode.left_rotation(node.leftChild)
        return RBnode.right_rotation(node)

    def rl_rotation(node):
        assert node.rightChild is not None
        node.rightChild = RBnode.right_rotation(node.rightChild)
        return RBnode.left_rotation(node)
    def inorder(node):
        if node is None:
            return
        RBnode.inorder(node.leftChild)
        print(node)
        RBnode.inorder(node.rightChild)

    def insert_node(node, value):
        if node is None:
            print(f"insert {value}")
            return RBnode(value, None, None, None, 0)
        if value < node.value:
            node.leftChild = RBnode.insert_node(node.leftChild,  value)
            print(f"{value} left")
        elif value > node.value:
            node.rightChild = RBnode.insert_node(node.rightChild,  value)
            print(f"{value}right")


class RBtree:
    def __init__(self):
        self.root = None
        print("init")

    def insert(self, value):
        if self.root is None:
            print("none")
            self.root = RBnode(value, None, None, None, 0)
        else:
            print("not none")
            self.root = RBnode.insert_node(self.root,  value)

    def inorder(self):
        RBnode.inorder(self.root)