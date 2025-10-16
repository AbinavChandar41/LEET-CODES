class Node:
    def __init__(self, data):
        self.data = data
        self.pointer = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            curr = self.head
            while (curr.pointer is not None):
                curr = curr.pointer
            curr.pointer = newnode

    def print(self):
        curr = self.head
        while (curr is not None):
            print(curr.data, end=" ")
            curr = curr.pointer
        print()

    def remove(self, data):
        if (self.head is not None):
            if (self.head.data == data):
                self.head = self.head.pointer
            else:
                curr = self.head
                while (curr.pointer is not None and curr.pointer.data != data):
                    curr = curr.pointer
                if curr.pointer is not None:
                    curr.pointer = curr.pointer.pointer
                else:
                    print(data, "is not in the linked list")
        else:
            print("linked list is empy")


link = LinkedList()
link.add(2)
link.add(3)
link.add(4)
link.add(5)
link.print()
link.remove(7)
link.remove(4)
link.print()