class RBtree:
    def __init__(self):
        self.root = None
        self.ll = False
        self.lr = False
        self.rr = False
        self.rl = False
        self.redRedConflict = False

    @property
    def black_height(self):
        return self.__black_height(self.root)
    
    @property
    def is_empty(self):
        if self.root is None:
            return True
        return False

    def __black_height(self, node):
        if node is None:
            return 0
        left_height = self.__black_height(node.leftChild)
        right_height = self.__black_height(node.rightChild)

        if left_height == -1 or right_height == -1 or left_height != right_height:
            return -1
        else:
            if node.color is self.RBnode.BLACK:
                return left_height + 1
            else:
                return left_height

    class RBnode:
        BLACK = 0
        RED = 1

        def __init__(
                self,
                data=None,
                parent=None,
                leftChild=None,
                rightChild=None,
                color=None):
            self.data = data
            self.parent = parent
            self.leftChild = leftChild
            self.rightChild = rightChild
            self.color = color

        def __str__(self):
            return f"data: {self.data}, color: {self.color}"

    def __right_rotation(self, node):
        x = node.leftChild
        y = x.rightChild
        x.rightChild = node
        node.leftChild = y
        node.parent = x
        if y is not None:
            y.parent = node
        return x

    def __left_rotation(self, node):
        x = node.rightChild
        y = x.leftChild
        x.leftChild = node
        node.rightChild = y
        node.parent = x
        if y is not None:
            y.parent = node
        return x

    def inorder_traverse(self, node):
        if node:
            yield from self.inorder_traverse(node.leftChild)
            yield node
            yield from self.inorder_traverse(node.rightChild)

    def preorder_traverse(self, node):
        if node:
            yield node
            yield from self.preorder_traverse(node.leftChild)
            yield from self.preorder_traverse(node.rightChild)

    def postorder_traverse(self, node):
        if node:
            yield from self.postorder_traverse(node.leftChild)
            yield from self.postorder_traverse(node.rightChild)
            yield node

    def __insert_node(self, node, data):
        if node is None:
            return self.RBnode(data, color=self.RBnode.RED)
        if data < node.data:
            node.leftChild = self.__insert_node(node.leftChild, data)
            node.leftChild.parent = node
            if node is not self.root:
                if (
                    node.color is self.RBnode.RED
                    and node.leftChild.color is self.RBnode.RED
                ):
                    self.redRedConflict = True
        else:
            node.rightChild = self.__insert_node(node.rightChild, data)
            node.rightChild.parent = node
            if node is not self.root:
                if (
                    node.color is self.RBnode.RED
                    and node.rightChild.color is self.RBnode.RED
                ):
                    self.redRedConflict = True
        node = self.__rotation_helper(node)
        node = self.__recolor(node)
        return node

    def __rotation_helper(self, node):
        if self.ll:
            node = self.__left_rotation(node)
            node.color = self.RBnode.BLACK
            node.leftChild.color = self.RBnode.RED
            self.ll = False
        elif self.rr:
            node = self.__right_rotation(node)
            node.color = self.RBnode.BLACK
            node.rightChild.color = self.RBnode.RED
            self.rr = False
        elif self.rl:
            node.rightChild = self.__right_rotation(node.rightChild)
            node.rightChild.parent = node
            node = self.__left_rotation(node)
            node.color = self.RBnode.BLACK
            node.leftChild.color = self.RBnode.RED
            self.rl = False
        elif self.lr:
            node.leftChild = self.__left_rotation(node.leftChild)
            node.leftChild.parent = node
            node = self.__right_rotation(node)
            node.color = self.RBnode.BLACK
            node.rightChild.color = self.RBnode.RED
            self.lr = False
        return node

    def __recolor(self, node):
        if self.redRedConflict:
            if node.parent.rightChild is node:  # wujek na lewo
                if (
                    node.parent.leftChild is None
                    or node.parent.leftChild.color is self.RBnode.BLACK
                ):
                    if (
                        node.leftChild is not None
                        and node.leftChild.color is self.RBnode.RED
                    ):
                        self.rl = True
                    elif (
                        node.rightChild is not None
                        and node.rightChild.color is self.RBnode.RED
                    ):
                        self.ll = True
                else:
                    node.parent.leftChild.color = self.RBnode.BLACK
                    node.color = self.RBnode.BLACK
                    if node.parent is not self.root:
                        node.parent.color = self.RBnode.RED
            else:  # wujek na prawo
                if (
                    node.parent.rightChild is None
                    or node.parent.rightChild.color is self.RBnode.BLACK
                ):
                    if (
                        node.leftChild is not None
                        and node.leftChild.color is self.RBnode.RED
                    ):
                        self.rr = True
                    elif (
                        node.rightChild is not None
                        and node.rightChild.color is self.RBnode.RED
                    ):
                        self.lr = True
                else:
                    node.parent.rightChild.color = self.RBnode.BLACK
                    node.color = self.RBnode.BLACK
                    if node.parent is not self.root:
                        node.parent.color = self.RBnode.RED
            self.redRedConflict = False
        return node

    def __search_node(self, node, data):
        if node is None or node.data == data:
            return node
        if node.data < data:
            return self.__search_node(node.rightChild, data)
        else:
            return self.__search_node(node.leftChild, data)

    def insert(self, *values):  # O(log n)
        for data in values:
            if self.root:
                self.root = self.__insert_node(self.root, data)
            else:
                self.root = self.RBnode(data, None, color=self.RBnode.BLACK)

    def search(self, data):  # O(log n)
        return self.__search_node(self.root, data)

    def clear(self):  # O(1)
        self.root = None
        self.ll = False
        self.lr = False
        self.rr = False
        self.rl = False
        self.redRedConflict = False

    def inorder_print(self):
        for node in self.inorder_traverse(self.root):
            print(
                f"node={node}, parent={node.parent}, 
                leftChild={node.leftChild}, rightChild={node.rightChild}"
            )

    def preorder_print(self):
        for node in self.preorder_traverse(self.root):
            print(
                f"node={node}, parent={node.parent}, 
                leftChild={node.leftChild}, rightChild={node.rightChild}"
            )

    def postorder_print(self):
        for node in self.postorder_traverse(self.root):
            print(
                f"node={node}, parent={node.parent}, 
                leftChild={node.leftChild}, rightChild={node.rightChild}"
            )
    def tree_print(self):
        self.tree_print_helper(self.root)

    def tree_print_helper(self,node,level=0):
        if node is None:
            return
        self.tree_print_helper(node.rightChild,level+1)
        color = 'R' if node.color is self.RBnode.RED else 'B'
        print(f"{'    '*level} {node.data}({color})")
        self.tree_print_helper(node.leftChild,level+1)
        
