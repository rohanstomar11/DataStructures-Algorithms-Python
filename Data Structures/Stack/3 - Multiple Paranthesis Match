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
            return
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


def match(a, b):
    if(a == '(' and b == ')'):
        return 1
    if(a == '[' and b == ']'):
        return 1
    if(a == '{' and b == '}'):
        return 1
    return 0


def parenthesisMatch(exp):
    stack = Stack()
    for s in exp:
        if(s == '(' or s == '[' or s == '{'):
            stack.push(s)
        elif (s == ')' or s == ']' or s == '}'):
            if(stack.isEmpty()):
                return 0
            else:
                popped = stack.pop()
                if not (match(popped, s)):
                    return 0
    if(stack.isEmpty()):
        return 1
    else:
        return 0


exp = "[4-6]((8){(9-8)})"
if (parenthesisMatch(exp)):
    print("The parenthesis is matching!")
else:
    print("The parenthesis is not matching!")
