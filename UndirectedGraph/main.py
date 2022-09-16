class Graph:
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size
    
    def add_edge(self,v1,v2):
        if v1==v2:
            print("Same vertex %d and %d" % (v1,v2))
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
    
    def remove_edge(self,v1,v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1,v2))
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def dfs(self, s, v = []):
        v.append(s)

        for i in range(len(self.adjMatrix)):
            if self.adjMatrix[s][i] == 1 and i not in v:
                self.dfs(i, v)
        return v

    def print_matrix(self):
        for i in self.adjMatrix:
            print(i)

if __name__ == "__main__":
    
    g = Graph(4)

    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(1,2)
    g.add_edge(1,3)
    g.add_edge(2,3)

    v = g.dfs(1)
    print(v)