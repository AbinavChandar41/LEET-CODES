class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, data):
        if not self.root:
            self.root = BSTNode(data)
            return
        self.recursiveAdd(data, self.root)

    def recursiveAdd(self, data, node):
        if data < node.data:
            if not node.left:
                node.left = BSTNode(data)
            else:
                self.recursiveAdd(data, node.left)
        elif data > node.data:
            if not node.right:
                node.right = BSTNode(data)
            else:
                self.recursiveAdd(data, node.right)

    def display(self):
        result = []
        self.inorderTraversal(self.root, result)
        print(result)

    def inorderTraversal(self, node, result):
        if not node:
            return None
        else:
            self.inorderTraversal(node.left, result)
            result.append(node.data)
            self.inorderTraversal(node.right, result)

    def preorderTraversal(self, node, result):
        if not node:
            return None
        else:
            result.append(node.data)
            self.preorderTraversal(node.left, result)
            self.preorderTraversal(node.right, result)

    def postorderTraversal(self, node, result):
        if not node:
            return None
        else:
            self.postorderTraversal(node.left, result)
            self.postorderTraversal(node.right, result)
            result.append(node.data)


bst = BinarySearchTree()
bst.add(5)
bst.add(3)
bst.add(1)
bst.add(4)
bst.add(6)
bst.display()
