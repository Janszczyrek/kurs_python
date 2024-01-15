class RBtree:
    def __init__(self):
        self.root = None
        self.ll = False
        self.lr = False
        self.rr = False
        self.rl = False
        self.redRedConflict = False
        print("init")

    class RBnode:
        BLACK = 0
        RED = 1
        def __init__(self, data=None, parent=None, leftChild=None, rightChild=None, color=None):
            self.data = data
            self.parent = parent
            self.leftChild = leftChild
            self.rightChild = rightChild
            self.color = color

        def __str__(self):
            return f"data: {self.data}, color: {self.color}"

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

    # def lr_rotation(node):
    #     assert node.leftChild is not None
    #     node.leftChild = RBnode.left_rotation(node.leftChild)
    #     return RBnode.right_rotation(node)

    # def rl_rotation(node):
    #     assert node.rightChild is not None
    #     node.rightChild = RBnode.right_rotation(node.rightChild)
    #     return RBnode.left_rotation(node)
    def inorder_node(self,node):
        if node is None:
            return
        self.inorder_node(node.leftChild)
        print(f"node={node}, parent={node.parent}, leftChild={node.leftChild}, rightChild={node.rightChild}")
        self.inorder_node(node.rightChild)
    def preorder_node(self,node):
        if node is None:
            return
        print(f"node={node}, parent={node.parent}, leftChild={node.leftChild}, rightChild={node.rightChild}")
        self.preorder_node(node.leftChild)
        self.preorder_node(node.rightChild)

    def insert_node(self, node, data):
        # self.redRedConflict = False
        if node is None:
            return self.RBnode(data,color=self.RBnode.RED)
        if data < node.data:
            node.leftChild = self.insert_node(node.leftChild,data)
            node.leftChild.parent = node
            if node is not self.root:
                if node.color is self.RBnode.RED and node.leftChild.color is self.RBnode.RED:
                    self.redRedConflict = True
        else:
            node.rightChild = self.insert_node(node.rightChild,data)
            node.rightChild.parent = node
            if node is not self.root:
                if node.color is self.RBnode.RED and node.rightChild.color is self.RBnode.RED:
                    self.redRedConflict = True
        node = self.rotation_helper(node)
        node = self.recolor(node)
        # print(f"root{self.root}")
        #self.inorder()
        return node

    def rotation_helper(self,node):
        print("___rotation helper___")
        print(node,node.parent)
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
        print(node,node.parent,node.leftChild,node.rightChild)
        print("___ENDrotation helperEND___")
        return node
        
    def recolor(self,node):
        if self.redRedConflict:
            print("recolor helper")
            if node.parent.rightChild is node: # uncle is on the left
                if node.parent.leftChild is None or node.parent.leftChild.color is self.RBnode.BLACK:
                    if node.leftChild is not None and node.leftChild.color is self.RBnode.RED:
                        print("right-left rotation")
                        self.rl = True
                    elif node.rightChild is not None and node.rightChild.color is self.RBnode.RED:
                        print("left-left rotation")
                        self.ll = True
                else:
                    node.parent.leftChild.color = self.RBnode.BLACK
                    node.color = self.RBnode.BLACK
                    if node.parent is not self.root:
                        node.parent.color = self.RBnode.RED
            else:
                if node.parent.rightChild is None or node.parent.rightChild.color is self.RBnode.BLACK:
                    if node.leftChild is not None and node.leftChild.color is self.RBnode.RED:
                        print("right-right rotation")
                        self.rr = True
                    elif node.rightChild is not None and node.rightChild.color is self.RBnode.RED:
                        print("left-right rotation")
                        self.lr = True
                else:
                    node.parent.rightChild.color = self.RBnode.BLACK
                    node.color = self.RBnode.BLACK
                    if node.parent is not self.root:
                        node.parent.color = self.RBnode.RED
            self.redRedConflict = False
        return node
    def insert(self, data):
        if self.root:
            print("not none")
            self.root = self.insert_node(self.root,data)
        else:
            print("none")
            self.root = self.RBnode(data,None,color=self.RBnode.BLACK)

    def inorder(self):
        self.inorder_node(self.root)
    def preorder(self):
        self.preorder_node(self.root)
