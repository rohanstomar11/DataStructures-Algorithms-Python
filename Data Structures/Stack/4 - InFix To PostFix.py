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

    def stackTop(self):
        if(self.isEmpty()):
            return -1
        else:
            top = self.top
            return top.data


def isOperator(ch):
    if(ch == '+' or ch == '-' or ch == '*' or ch == '/'):
        return 1
    return 0


def checkPrecedence(ch):
    if (ch == '*' or ch == '/'):
        return 3
    elif (ch == '+' or ch == '-'):
        return 2
    else:
        return 0


def infixToPostfix(exp):
    stack = Stack()
    new = ""
    for s in exp:
        if not isOperator(s):
            new = new + s
        else:
            if(checkPrecedence(s) >= checkPrecedence(stack.stackTop())):
                stack.push(s)
            else:
                new = new + str(stack.pop())
    while(not(stack.isEmpty())):
        new = new + str(stack.pop())
    return new


infix = "a+b+d-c"
print("Postfix is : ", infixToPostfix(infix))
