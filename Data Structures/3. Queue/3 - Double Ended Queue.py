class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def display(self):
        front = self.front
        if(front == None):
            print("Queue is Empty!")
        else:
            print(front.data)
            while(front.next != None):
                front = front.next
                print(front.data)

    def isEmpty(self):
        front = self.front
        if (front == None):
            return 1
        else:
            return 0

    def isFull(self):
        node = Node(11)
        if(node == None):
            return 1
        else:
            return 0

    def enqueueFront(self, data):
        front = self.front
        rear = self.rear
        if(self.isFull()):
            print("Memory Full!")
        else:
            if(self.isEmpty()):
                node = Node(data)
                self.front = node
                self.rear = node
            else:
                if(front == rear):
                    node = Node(data)
                    front.next = node
                    self.rear = node
                else:
                    node = Node(data)
                    node.next = front
                    self.front = node

    def enqueueRear(self, data):
        front = self.front
        rear = self.rear
        if(self.isFull()):
            print("Memory Full!")
        else:
            if(self.isEmpty()):
                node = Node(data)
                self.front = node
                self.rear = node
            else:
                if(front == rear):
                    node = Node(data)
                    front.next = node
                    self.rear = node
                else:
                    node = Node(data)
                    rear.next = node
                    self.rear = node

    def dequeueFront(self):
        front = self.front
        rear = self.rear
        if(self.isEmpty()):
            print("Queue Empty!")
        else:
            print("Processed Front: ", front.data)
            if(front == rear):
                self.front = None
                self.rear = None
            else:
                front = front.next
                self.front = front

    def dequeueRear(self):
        front = self.front
        rear = self.rear
        if(self.isEmpty()):
            print("Queue Empty!")
        else:
            print("Processed Rear: ", rear.data)
            if(front == rear):
                self.front = None
                self.rear = None
            else:
                while(front.next != rear):
                    front = front.next
                front.next = None
                self.rear = front

    def getFront(self):
        front = self.front
        return front.data

    def getRear(self):
        rear = self.rear
        return rear.data


queue = Queue()

print("--->")
queue.display()
print("---")

queue.enqueueRear(22)
queue.enqueueRear(33)
queue.enqueueFront(11)
queue.enqueueRear(44)
queue.enqueueFront(00)

print("--->")
queue.display()
print("---")

print("--->")
print("Front: ", queue.getFront())
print("Rear: ", queue.getRear())
print("---")

queue.dequeueFront()
queue.dequeueFront()
queue.dequeueRear()
queue.dequeueRear()

print("--->")
queue.display()
print("---")

queue.dequeueFront()

print("--->")
queue.display()
print("---")
