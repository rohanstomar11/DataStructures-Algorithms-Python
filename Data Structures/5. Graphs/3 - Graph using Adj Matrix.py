class Graph:
    def __init__(self, n):
        self.vertices = n
        self.matrix = []
        for i in range(n):
            self.matrix.append([0 for i in range(n)])

    def add(self, data1, data2):
        self.matrix[data1][data2] = 1
        self.matrix[data2][data1] = 1

    def displayGraph(self):
        for i in range(self.vertices):
            print(self.matrix[i])


graph = Graph(5)

graph.add(0, 1)
graph.add(1, 3)
graph.add(0, 2)
graph.add(2, 3)
graph.add(3, 4)

graph.displayGraph()
