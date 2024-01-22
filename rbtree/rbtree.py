class RBtree:
    def __init__(self):
        self.root = None
        self.ll = False
        self.lr = False
        self.rr = False
        self.rl = False
        self.redRedConflict = False
        print("init")

    @property
    def black_height(self):
        return self.__black_height(self.root)

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
            self, data=None, parent=None, leftChild=None, rightChild=None, color=None
        ):
            self.data = data
            self.parent = parent
            self.leftChild = leftChild
            self.rightChild = rightChild
            self.color = color

        def __str__(self):
            return f"data: {self.data}, color: {self.color}"
        
        @property
        def sibling(self):
            if self.parent is None:
                return None
            if self is self.parent.leftChild:
                return self.parent.rightChild
            else:
                return self.parent.leftChild
        @property
        def has_red_child(self):
            if (
                self.rightChild is not None
                and self.rightChild.color is self.RED
                or self.leftChild is not None
                and self.leftChild.color is self.RED
            ):
                return True
            else:
                return False
    
        @property
        def successor(self):
            x = self
            while x.leftChild is not None:
                x = x.leftChild
            return x

    def right_rotation(self, node):
        x = node.leftChild
        y = x.rightChild
        x.rightChild = node
        node.leftChild = y
        node.parent = x
        if y is not None:
            y.parent = node
        return x

    def left_rotation(self, node):
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

    def insert_node(self, node, data):
        # self.redRedConflict = False
        if node is None:
            return self.RBnode(data, color=self.RBnode.RED)
        if data < node.data:
            node.leftChild = self.insert_node(node.leftChild, data)
            node.leftChild.parent = node
            if node is not self.root:
                if (
                    node.color is self.RBnode.RED
                    and node.leftChild.color is self.RBnode.RED
                ):
                    self.redRedConflict = True
        else:
            node.rightChild = self.insert_node(node.rightChild, data)
            node.rightChild.parent = node
            if node is not self.root:
                if (
                    node.color is self.RBnode.RED
                    and node.rightChild.color is self.RBnode.RED
                ):
                    self.redRedConflict = True
        node = self.rotation_helper(node)
        node = self.recolor(node)
        return node




    def replacement_node(self, node):
        if node.leftChild is None and node.rightChild is None:
            return None
        if node.leftChild is not None and node.rightChild is not None:
            return self.successor(node.rightChild)
        if node.leftChild is not None:
            return node.leftChild
        else:
            return node.rightChild

    def delete_node(self, node):
        # if node.color is self.RBnode.RED:
        #     inorder_successor = self.replacement_node(node)

        replacement = self.replacement_node(node)
        isDoubleBlack = (
            replacement is None or replacement.color is self.RBnode.BLACK
        ) and (node.color is self.RBnode.BLACK)
        parent = node.parent
        sibling = node.sibling


        if replacement is None:
            if node is self.root:
                self.clear()
            else:
                if isDoubleBlack:
                    self.double_black_restore(node)
                else:
                    if sibling is not None:
                        sibling.color = self.RBnode.RED
                if node is parent.leftChild:
                    parent.leftChild = None
                else:
                    parent.rightChild = None
            return
        if node.leftChild is None or node.rightChild is None:
            if node is self.root:
                node.data = replacement.data
                node.leftChild = None
                node.rightChild = None
            else:
                if node is parent.leftChild:
                    parent.leftChild = replacement
                else:
                    parent.rightChild = replacement
                replacement.parent = parent
                if isDoubleBlack:
                    self.double_black_restore(replacement)
                else:
                    replacement.color = self.RBnode.BLACK
        else:
            x = node.data
            node.data = replacement.data
            replacement.data = x
            self.delete_node(replacement)

    def double_black_restore(self, node):
        if node is self.root:
            return
        parent = node.parent
        sibling = node.sibling
        if sibling is None:
            self.double_black_restore(parent)
        else:
            if sibling.color is self.RBnode.RED:
                parent.color = self.RBnode.RED
                sibling.color = self.RBnode.BLACK

                if sibling is sibling.parent.leftChild:
                    parent = self.right_rotation(parent)
                else:
                    parent = self.left_rotation(parent)
                self.double_black_restore(node)
            else:
                if node.has_red_child:
                    if (
                        sibling.leftChild is not None
                        and sibling.leftChild.color is self.RBnode.RED
                    ):
                        if sibling is sibling.parent.leftChild:
                            sibling.leftChild.color = sibling.color
                            sibling.color = parent.color
                            parent = self.right_rotation(parent)
                        else:
                            sibling.leftChild.color = parent.color
                            sibling = self.right_rotation(sibling)
                            parent = self.left_rotation(parent)
                    else:
                        if sibling is sibling.parent.leftChild:
                            sibling.rightChild.color = parent.color
                            sibling = self.left_rotation(sibling)
                            parent = self.right_rotation(parent)
                        else:
                            sibling.rightChild.color = sibling.color
                            sibling.color = parent.color
                            parent = self.left_rotation(parent)

                else:
                    sibling.color = self.RBnode.RED
                    if parent.color is self.RBnode.BLACK:
                        self.double_black_restore(parent)
                    else:
                        parent.color = self.RBnode.BLACK

    def rotation_helper(self, node):
        print("___rotation helper___")
        print(node, node.parent)
        if self.ll:
            node = self.left_rotation(node)
            node.color = self.RBnode.BLACK
            node.leftChild.color = self.RBnode.RED
            self.ll = False
        elif self.rr:
            node = self.right_rotation(node)
            node.color = self.RBnode.BLACK
            node.rightChild.color = self.RBnode.RED
            self.rr = False
        elif self.rl:
            node.rightChild = self.right_rotation(node.rightChild)
            node.rightChild.parent = node
            node = self.left_rotation(node)
            node.color = self.RBnode.BLACK
            node.leftChild.color = self.RBnode.RED
            self.rl = False
        elif self.lr:
            node.leftChild = self.left_rotation(node.leftChild)
            node.leftChild.parent = node
            node = self.right_rotation(node)
            node.color = self.RBnode.BLACK
            node.rightChild.color = self.RBnode.RED
            self.lr = False
        print(node, node.parent, node.leftChild, node.rightChild)
        print("___ENDrotation helperEND___")
        return node

    def recolor(self, node):
        if self.redRedConflict:
            print("recolor helper")
            if node.parent.rightChild is node:  # uncle is on the left
                if (
                    node.parent.leftChild is None
                    or node.parent.leftChild.color is self.RBnode.BLACK
                ):
                    if (
                        node.leftChild is not None
                        and node.leftChild.color is self.RBnode.RED
                    ):
                        print("right-left rotation")
                        self.rl = True
                    elif (
                        node.rightChild is not None
                        and node.rightChild.color is self.RBnode.RED
                    ):
                        print("left-left rotation")
                        self.ll = True
                else:
                    node.parent.leftChild.color = self.RBnode.BLACK
                    node.color = self.RBnode.BLACK
                    if node.parent is not self.root:
                        node.parent.color = self.RBnode.RED
            else:
                if (
                    node.parent.rightChild is None
                    or node.parent.rightChild.color is self.RBnode.BLACK
                ):
                    if (
                        node.leftChild is not None
                        and node.leftChild.color is self.RBnode.RED
                    ):
                        print("right-right rotation")
                        self.rr = True
                    elif (
                        node.rightChild is not None
                        and node.rightChild.color is self.RBnode.RED
                    ):
                        print("left-right rotation")
                        self.lr = True
                else:
                    node.parent.rightChild.color = self.RBnode.BLACK
                    node.color = self.RBnode.BLACK
                    if node.parent is not self.root:
                        node.parent.color = self.RBnode.RED
            self.redRedConflict = False
        return node

    def search_node(self, node, data):
        if node is None or node.data == data:
            return node
        if node.data < data:
            return self.search_node(node.rightChild, data)
        else:
            return self.search_node(node.leftChild, data)

    def insert(self, *values):
        for data in values:
            if self.root:
                print("not none")
                self.root = self.insert_node(self.root, data)
            else:
                print("none")
                self.root = self.RBnode(data, None, color=self.RBnode.BLACK)

    def delete(self, data):
        node = self.search(data)
        self.delete_node(node)

    def search(self, data):
        return self.search_node(self.root, data)

    def clear(self):
        self.root = None
        self.ll = False
        self.lr = False
        self.rr = False
        self.rl = False
        self.redRedConflict = False

    def inorder_print(self):
        for node in self.inorder_traverse(self.root):
            print(
                f"node={node}, parent={node.parent}, leftChild={node.leftChild}, rightChild={node.rightChild}"
            )

    def preorder_print(self):
        for node in self.preorder_traverse(self.root):
            print(
                f"node={node}, parent={node.parent}, leftChild={node.leftChild}, rightChild={node.rightChild}"
            )

    def postorder_print(self):
        for node in self.postorder_traverse(self.root):
            print(
                f"node={node}, parent={node.parent}, leftChild={node.leftChild}, rightChild={node.rightChild}"
            )
