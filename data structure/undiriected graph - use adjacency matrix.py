class Vertex:
    def __init__(self, n):
        self.name = n

class Graph:
    verteces = {}
    edges = []
    def add_vertex(self,vertex):
        v = Vertex(vertex)
        if vertex not in self.verteces:
            for row in self.edges:
                row.append(0)
            self.edges.append([0])
            # index
            self.verteces[v.name] = len(self.verteces)
            for i in range(len(self.edges) - 1):
                self.edges[len(self.verteces) - 1].append(0)

    def add_edges(self, m, n, weight = 1):
        if m in self.verteces and n in self.verteces:
            self.edges[self.verteces[m]][self.verteces[n]] = weight
            self.edges[self.verteces[n]][self.verteces[m]] = weight
            return True
        else:
            return False
    def print(self):
        n = list(self.verteces.keys())
        print(' ', end= ' ')
        for a in n:
            print(a, end = ' ')
        print()
        for j in range(len(self.edges)):
            print(n[j],  end = ' ')
            for k in range(len(self.edges)):
                print(self.edges[j][k], end = ' ')
            print()
    def pi(self):
        print(str(self.verteces))
g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_edges('A', 'B')
g.add_vertex('D')
g.add_vertex('C')
g.add_edges('A', 'C')
for i in range(ord('A'), ord('K')):
	g.add_vertex(chr(i))
edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
	g.add_edges(edge[:1], edge[1:])
g.print()