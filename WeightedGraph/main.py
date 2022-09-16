
class Graph:

    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size
    
    def add_edge(self,v1,v2,weight='e'):
        self.adjMatrix[v1][v2] = weight

    def remove_edge(self,v1,v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1,v2))
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def dfs(self, s, v = []):
        v.append(s)

        for i in range(len(self.adjMatrix)):
            if self.adjMatrix[s][i] != 0 and i not in v:
                self.dfs(i, v)
        return v

    def print_matrix(self):
        for i in self.adjMatrix:
            print(i)

if __name__ == "__main__":
    
    g = Graph(7)

    g.add_edge(0,0,0.35)
    g.add_edge(0,1)
    g.add_edge(0,3,0.39)
    g.add_edge(1,3,0.39)
    g.add_edge(1,0)
    g.add_edge(2,4,0.70)
    g.add_edge(4,2,0.90)
    g.add_edge(3,3,0.3)
    g.add_edge(3,0,0.91)
    g.add_edge(3,1,0.91)
    g.add_edge(3,4)
    g.add_edge(4,3)
    g.add_edge(4,4,0.3)
    g.add_edge(3,5,0.3)
    g.add_edge(5,3,0.9)
    g.add_edge(4,5,0.3)
    g.add_edge(5,4,0.9)
    g.add_edge(5,6)
    g.add_edge(6,5)
    g.add_edge(6,6)

    g.print_matrix()