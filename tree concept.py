class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []


class Tree:
    def __init__(self):
        self.root = None

    def add(self, data, parentdata=None):
        node = TreeNode(data)
        if not self.root:
            self.root = node
            return

        parentnode = self.findnode(parentdata, self.root)

        if not parentnode:
            print("the number is not found in the tree")
            return
        parentnode.children.append(node)

    def findnode(self, data, node):
        if node.data == data:
            return node

        for child in node.children:
            nodefound = self.findnode(data, child)
            if nodefound is not None:
                return nodefound

        return None

    def display(self, depth=0, node=None):
        if not node:
            node = self.root
        print(" " * depth, node.data)
        for child in node.children:
            self.display(depth + 1, child)

    def remove(self, data):
        if not self.root:
            print("tree is empty")
            return
        if self.root.data == data:
            self.root = None
            return
        parentnode = self.findparentnode(data, self.root)
        if parentnode:
            for child in parentnode.children:
                if child.data == data:
                    parentnode.children.remove(child)

    def findparentnode(self, data, node):
        for child in node.children:
            if child.data == data:
                return node
            nodefound = self.findparentnode(data, child)
            if nodefound:
                return nodefound
        return None


tree = Tree()
tree.add(3)
tree.add(4, 3)
tree.add(5, 3)
tree.add(6, 5)
tree.display()
tree.remove(6)
tree.display()