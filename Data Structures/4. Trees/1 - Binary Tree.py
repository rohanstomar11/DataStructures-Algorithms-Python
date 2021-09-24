class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


class Tree:
    def __init__(self, node):
        self.root = node

    def preOrderTraversal(self, node):
        if node == None:
            return
        else:
            print(node.data)
            self.preOrderTraversal(node.left)
            self.preOrderTraversal(node.right)

    def postOrderTraversal(self, node):
        if node == None:
            return
        else:
            self.postOrderTraversal(node.left)
            self.postOrderTraversal(node.right)
            print(node.data)

    def inOrderTraversal(self, node):
        if node == None:
            return
        else:
            self.inOrderTraversal(node.left)
            print(node.data)
            self.inOrderTraversal(node.right)


a = Node(5)
b = Node(3)
c = Node(7)
d = Node(2)
e = Node(4)
f = Node(6)
g = Node(8)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
tree = Tree(a)

print("Pre Order--->")
tree.preOrderTraversal(a)
print("---")
print("Post Order--->")
tree.postOrderTraversal(a)
print("---")
print("In Order--->")
tree.inOrderTraversal(a)
print("---")
