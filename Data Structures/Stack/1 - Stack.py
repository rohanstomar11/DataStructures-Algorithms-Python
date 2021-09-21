class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.bottom = None
        self.top = None

    def isEmpty(self):
        top = self.top
        if(top == None):
            return 1
        else:
            return 0

    def isFull(self):
        node = Node(0)
        if (node == None):
            return 1
        else:
            return 0

    def display(self):
        bottom = self.bottom
        top = self.top
        if(self.isEmpty()):
            print("Stack is Empty, Nothing to display!")
        else:
            print(top.data)
            while(top != bottom):
                top = top.next
                print(top.data)

    def push(self, data):
        if(self.isFull()):
            print("Stack Full!")
        else:
            if(self.isEmpty()):
                node = Node(data)
                self.top = node
                self.bottom = node
            else:
                top = self.top
                node = Node(data)
                node.next = top
                self.top = node

    def pop(self):
        if(self.isEmpty()):
            print("Nothing to Pop, Stack is Empty!")
            return -1
        else:
            bottom = self.bottom
            top = self.top
            if(top == bottom):
                data = top.data
                self.top = None
                self.bottom = None
                return data
            else:
                data = top.data
                top = top.next
                self.top = top
                return data

    def stackTop(self):
        top = self.top
        return top.data

    def stackBottom(self):
        bottom = self.bottom
        return bottom.data


stack = Stack()
print("--->")
stack.display()
print("---")
stack.push(55)
stack.push(66)
stack.push(77)
print("--->")
stack.display()
print("---")
print("Top: ", stack.stackTop())
print("Bottom: ", stack.stackBottom())
print("---")
print("Element Popped: ", stack.pop())
print("Element Popped: ", stack.pop())
print("--->")
stack.display()
print("---")
print("Element Popped: ", stack.pop())
print("--->")
stack.display()
print("---")
