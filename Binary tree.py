class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, data):
        if not self.root:
            self.root = Node(data)
            return
        self.recursiveAdd(data, self.root)

    def recursiveAdd(self, data, node):
        if node.left is None:
            node.left = Node(data)
        elif node.right is None:
            node.right = Node(data)
        else:
            self.recursiveAdd(data, node.left)

    def display(self, depth=0, node=None):
        if node is None:
            node = self.root
        print(" " * depth, node.data)

        if node.left is not None:
            self.display(depth + 1, node.left)
        if node.right is not None:
            self.display(depth + 1, node.right)

    def search(self,data):
        nodefound=self.recursivesearch(data,self.root)
        if nodefound:
            print("true")
        else:
            print("false")

    def recursivesearch(self,data,node):
        if not node or node.data==data:
            return node
        return self.recursivesearch(data,node.left) or self.recursivesearch(data,node.right)


binarytree = BinaryTree()
binarytree.add(5)
binarytree.add(3)
binarytree.add(1)
binarytree.add(5)
binarytree.add(4)
binarytree.search(8)
binarytree.display()