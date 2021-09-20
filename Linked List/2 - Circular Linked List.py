class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class circularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def displayFront(self):
        head = self.head
        if(head == None):
            print("Linked List(F) is Empty!")
        else:
            while(head != None):
                print(head.data)
                head = head.next

    def displayBack(self):
        tail = self.tail
        if(tail == None):
            print("Linked List(B) is Empty!")
        else:
            while(tail != None):
                print(tail.data)
                tail = tail.prev

    def addNodeAtEnd(self, data):
        head = self.head
        tail = self.tail
        node = Node(data)
        if(head == None):
            self.head = node
            self.tail = node
        else:
            if(head == tail):
                head.next = node
                node.prev = head
                self.tail = node
            else:
                tail.next = node
                node.prev = tail
                self.tail = node

    def addNodeAtFront(self, data):
        head = self.head
        tail = self.tail
        node = Node(data)
        if(head == None):
            self.head = node
            self.tail = node
        else:
            head.prev = node
            node.next = head
            self.head = node


circ = circularLinkedList()
print("--->")
circ.displayFront()
circ.addNodeAtEnd(5)
print("--->")
circ.displayFront()
circ.addNodeAtEnd(6)
print("--->")
circ.displayBack()
circ.addNodeAtFront(4)
print("--->")
circ.displayFront()
circ.addNodeAtFront(3)
print("--->")
circ.displayBack()
