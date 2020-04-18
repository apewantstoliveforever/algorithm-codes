class Vertex:
    def __init__(self, n):
        self.name = n
        self.value = []

class Graph:
    vertices = {}
    def add_vertex(self, vertex):
        v = Vertex(vertex)
        if vertex not in self.vertices:
            self.vertices[vertex] = v.value
            return True

    def add_edges(self, m, n):
        if m in self.vertices and n in self.vertices:
            if n not in self.vertices[m]:
                self.vertices[m].append(n)
            if m not in self.vertices[n]:
                self.vertices[n].append(m)
            return True
        else:
            return False

    def print(self):
        for i in self.vertices:
            print( str(i) + " " + str(self.vertices[i]))
g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_edges('A','B')
g.add_edges('D','C')
g.add_vertex('E')
edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
	g.add_edges(edge[:1], edge[1:])

g.print()



