class Node:
    def __init__(self, data):
        self.vertex = data
        self.next = None


class Graph:
    def __init__(self, n):
        self.vertices = n
        self.graph = [None] * self.vertices

    def add(self, data1, data2):
        node = Node(data2)
        node.next = self.graph[data1]
        self.graph[data1] = node

        node = Node(data1)
        node.next = self.graph[data2]
        self.graph[data2] = node

    def displayGraph(self):
        for i in range(self.vertices):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


graph = Graph(5)
graph.add(0, 1)
graph.add(0, 4)
graph.add(1, 2)
graph.add(1, 3)
graph.add(1, 4)
graph.add(2, 3)
graph.add(3, 4)

graph.displayGraph()
