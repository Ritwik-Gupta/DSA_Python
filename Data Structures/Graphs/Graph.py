class Graph:
    def __init__(self):
        self.adj_list = dict()

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def print_graph(self):
        print(self.adj_list)


g1 = Graph()

g1.add_vertex('A')
g1.add_vertex('B')
g1.add_vertex('C')

g1.add_edge('B','C')

g1.print_graph()

