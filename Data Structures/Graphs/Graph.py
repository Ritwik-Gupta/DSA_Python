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
    
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False
    
    def print_graph(self):
        print(self.adj_list)


g1 = Graph()

g1.add_vertex('A')
g1.add_vertex('B')
g1.add_vertex('C')
g1.add_vertex('D')

g1.add_edge('B','C')
g1.add_edge('A','B')
g1.add_edge('A','C')
g1.add_edge('C','D')

g1.print_graph()

g1.remove_edge('A', 'B')
g1.print_graph()

g1.remove_vertex('A')
g1.print_graph()
