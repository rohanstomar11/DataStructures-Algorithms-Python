class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None

    def addNodeAtFirst(self, data):
        head = self.head
        if(head == None):
            self.head = Node(data)
        else:
            node = Node(data)
            node.next = head
            self.head = node

    def addNodeAtLast(self, data):
        head = self.head
        if (head == None):
            self.head = Node(data)
        else:
            while(head.next != None):
                head = head.next
            head.next = Node(data)

    def addNodeAtIndex(self, data, index):
        head = self.head
        for i in range(index-1):
            head = head.next
        node = Node(data)
        node.next = head.next
        head.next = node

    def deleteNodeAtFirst(self):
        head = self.head
        if(head == None):
            print("Unable to delete, Linked List is empty")
        else:
            if(head.next == None):
                self.head = None
            else:
                self.head = head.next

    def deleteNodeAtLast(self):
        head = self.head
        if(head == None):
            print("Unable to Delete, Linked List is Empty!")
        else:
            if(head.next == None):
                self.head = None
            else:
                while((head.next).next != None):
                    head = head.next
                head.next = None

    def deleteNodeAtIndex(self, index):
        head = self.head
        if(head == None):
            print("Unable to Delete, Linked List is Empty!")
        else:
            for i in range(index-1):
                head = head.next
            head.next = (head.next).next

    def deleteNodeByValue(self, value):
        head = self.head
        if(head == None):
            print("unable to delete, Linked List Empty!")
        else:
            if(head.data == value):
                self.head = None
            else:
                while((head.next).data != value):
                    head = head.next
                head.next = (head.next).next

    def display(self):
        head = self.head
        if(head == None):
            print("Linked List is Empty!")
        else:
            while(head != None):
                print(head.data)
                head = head.next


List = linkedList()
print("--->")
List.display()
List.addNodeAtLast(55)
print("--->")
List.display()
List.addNodeAtFirst(33)
print("--->")
List.display()
List.addNodeAtIndex(44, 1)
print("--->")
List.display()
List.addNodeAtIndex(66, 3)
print("--->")
List.display()
List.deleteNodeAtIndex(1)
print("--->")
List.display()
List.deleteNodeAtLast()
print("--->")
List.display()
List.deleteNodeAtFirst()
print("--->")
List.display()
List.deleteNodeByValue(55)
print("--->")
List.display()
