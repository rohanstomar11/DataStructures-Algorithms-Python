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
        # Code to check whether the tree is BST or not.
        pass

    def checkData(self, root, data):
        # Code to check if a number(data) is present in BST or not.
        pass


bst = BST()
root = bst.insertNode(bst.getRoot(), 11)
root = bst.insertNode(bst.getRoot(), 5)
root = bst.insertNode(bst.getRoot(), 33)
root = bst.insertNode(bst.getRoot(), 1)
root = bst.insertNode(bst.getRoot(), 7)
root = bst.insertNode(bst.getRoot(), 22)
root = bst.insertNode(bst.getRoot(), 44)
bst.inOrderTraversal(bst.getRoot())
