class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def insertNode(self, root, data):
        if self.root is None:
            self.root = Node(data)
            return
        else:
            if root is None:
                root = Node(data)
                return root
            else:
                if(data < root.data):
                    root.left = self.insertNode(root.left, data)
                else:
                    root.right = self.insertNode(root.right, data)
            return root

    def inOrderTraversal(self, node):
        if node:
            self.inOrderTraversal(node.left)
            print(node.data)
            self.inOrderTraversal(node.right)

    def isBST(self, root):
        if root is None:
            return 1
        if (root.left is not None and root.left.data > root.data):
            return 0
        if(root.right is not None and root.right.data < root.data):
            return 0
        if(not(self.isBST(root.left)) or not(self.isBST(root.right))):
            return 0
        return 1

    def checkData(self, root, data):
        if root is None:
            return False
        if root.data == data:
            return True
        left = self.checkData(root.left, data)
        if left:
            return True
        right = self.checkData(root.right, data)
        return right


bst = BST()

root = bst.insertNode(bst.getRoot(), 11)
root = bst.insertNode(bst.getRoot(), 5)
root = bst.insertNode(bst.getRoot(), 33)
root = bst.insertNode(bst.getRoot(), 1)
root = bst.insertNode(bst.getRoot(), 7)
root = bst.insertNode(bst.getRoot(), 22)
root = bst.insertNode(bst.getRoot(), 44)

bst.inOrderTraversal(bst.getRoot())
print("---")

if(bst.isBST(bst.getRoot())):
    print("It is a Binary Search Tree!")
else:
    print("It is not a Binary Search Tree!")
print("---")

key = 11
if(bst.checkData(bst.getRoot(), key)):
    print(key, "exists in BST!")
else:
    print(key, "doesn't exists in BST!")
