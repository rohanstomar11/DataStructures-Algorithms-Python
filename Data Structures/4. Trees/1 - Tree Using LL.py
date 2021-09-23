class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        root = self.root
        if(root==None):
            root = Node(data)
            self.root = root
        else:
            if(root.left==None):
                