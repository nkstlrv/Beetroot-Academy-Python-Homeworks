class Vertex:

    def __init__(self, name, data):
        self.name = name
        self.data = data
        self.neighbours = {}

    def __str__(self):
        return f"Vertex {self.name}"

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def new_neighbour(self, new_vert, weight):
        if new_vert not in self.neighbours:
            self.neighbours[new_vert] = weight
            return True
        else:
            return False

    def show_neighbours(self):
        n_list = []
        for n in self.neighbours:
            n_list.append(n)
        return n_list

    def show_connections(self):
        res = f"({self.name}) "
        for k, v in self.neighbours.items():
            res += f"<- {v} -> ({k}) "
        return res


class Graph:
    def __init__(self):
        self.vertexes = {}
        self.size = 0
        self.edges_amount = 0

    def get_vertexes(self):
        return list(self.vertexes.keys())

    def add_vertex(self, vert_name, vert_data):
        if vert_name not in self.get_vertexes():
            new_vert = Vertex(vert_name, vert_data)
            self.vertexes[vert_name] = new_vert
            self.size += 1
            return True
        else:
            return False

    def add_edge(self, fm, to, weight):
        if fm in self.vertexes and to in self.vertexes:
            self.vertexes[fm].new_neighbour(to, weight)
            self.vertexes[to].new_neighbour(fm, weight)
            self.edges_amount += 1
            return True
        else:
            return False

    def remove_vertex(self, rem_vertex):
        if rem_vertex in self.get_vertexes():
            for vertex in self.vertexes.values():
                if rem_vertex in vertex.show_neighbours():
                    vertex.neighbours.pop(rem_vertex)
            self.vertexes.pop(rem_vertex)
            self.size -= 1
            return True
        else:
            return False

    def brake_edge(self, fm, to):
        if fm in self.get_vertexes() and to in self.get_vertexes():
            if fm in self.vertexes[to].neighbours and to in self.vertexes[fm].neighbours:
                self.vertexes[fm].neighbours.pop(to)
                self.vertexes[to].neighbours.pop(fm)
                self.edges_amount -= 1
                return True
            return False
        return False

    def get_edges(self):
        edges = []
        for vertexes in self.vertexes.values():
            for neighbour, weight in vertexes.neighbours.items():
                edges.append((vertexes.name, weight, neighbour))
        return tuple(edges)


if __name__ == "__main__":
    g_1 = Graph()
    g_1.add_vertex('a', 'hello')
    g_1.add_vertex('b', 'there')
    g_1.add_vertex('c', [1, 2, 3])
    g_1.add_edge('a', 'b', 3)
    g_1.add_edge('a', 'c', 4)
    print(g_1.get_edges())
    g_1.remove_vertex('c')
    print(g_1.get_edges())
    g_1.brake_edge('a', 'b')
    print(g_1.get_edges())
    print(g_1.get_vertexes())