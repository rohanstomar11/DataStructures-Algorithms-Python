class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class doubleLinkedList:
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

    def addNodeAtIndex(self, data, index):
        head = self.head
        tail = self.tail
        node = Node(data)
        for i in range(index-1):
            head = head.next
        next = head.next
        node.prev = head
        node.next = next
        next.prev = node
        head.next = node

    def deleteNodeAtEnd(self):
        head = self.head
        tail = self.tail
        if(head == None):
            print("Unable to delete, Linked List Empty!")
        else:
            if(head == tail):
                self.head = None
                self.tail = None
            else:
                prev = tail.prev
                prev.next = None
                tail = None
                self.tail = prev

    def deleteNodeAtFront(self):
        head = self.head
        tail = self.tail
        if(head == None):
            print("Unable to delete, Linked List Empty!")
        else:
            if(head == tail):
                self.head = None
                self.tail = None
            else:
                next = head.next
                head = None
                next.prev = None
                self.head = next

    def deleteNodeAtIndex(self, index):
        head = self.head
        tail = self.tail
        if(head == None):
            print("Unable to delete, Linked List Empty!")
        else:
            for n in range(index-1):
                head = head.next
            next = head.next
            head.next = next.next
            (next.next).prev = head
            next = None

    def deleteNodeByValue(self, data):
        head = self.head
        tail = self.tail
        if(head == None):
            print("Unable to delete, Linked List Empty!")
        else:
            if(head.data == data):
                self.head = None
            else:
                while(head.data != data):
                    head = head.next
                prev = head.prev
                prev.next = head.next
                (head.next).prev = prev


doubleLL = doubleLinkedList()
print("--->")
doubleLL.displayFront()
doubleLL.addNodeAtEnd(5)
print("--->")
doubleLL.displayFront()
doubleLL.addNodeAtEnd(6)
print("<---")
doubleLL.displayBack()
doubleLL.addNodeAtFront(4)
print("--->")
doubleLL.displayFront()
doubleLL.addNodeAtIndex(0, 2)
print("--->")
doubleLL.displayFront()
doubleLL.addNodeAtFront(3)
print("--->")
doubleLL.displayFront()
doubleLL.deleteNodeAtIndex(2)
print("--->")
print("--->")
doubleLL.displayFront()
doubleLL.deleteNodeByValue(0)
print("--->")
doubleLL.displayFront()
print("<---")
doubleLL.displayBack()
doubleLL.deleteNodeAtIndex(1)
print("--->")
doubleLL.displayFront()
doubleLL.deleteNodeAtEnd()
print("--->")
doubleLL.displayFront()
print("<---")
doubleLL.displayBack()
doubleLL.deleteNodeAtEnd()
print("--->")
doubleLL.displayFront()
print("<---")
doubleLL.displayBack()
