class Graph(dict):
    def __init__(self):
        self.graph = dict()
        self.edges = []

    def add(self, data1, data2):
        self.edges.append(str(data1)+str(data2))
        try:
            graph[data1] = graph[data1] + ',' + data2
        except KeyError:
            graph[data1] = data2
        try:
            graph[data2] = graph[data2] + ',' + data1
        except KeyError:
            graph[data2] = data1

    def displayVertices(self):
        print("Vertices -> ", list(graph.keys()))

    def displayEdges(self):
        print("Edges -> ", self.edges)


graph = Graph()
graph.add('A', 'B')
graph.add('A', 'C')
graph.add('B', 'D')
graph.add('C', 'D')
graph.add('D', 'E')

graph.displayVertices()
print("---")

graph.displayEdges()
print("---")

print("Graph -> ", graph)
