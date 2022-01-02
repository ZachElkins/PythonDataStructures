from data_structures.queue import Queue


class Graph:
    """
    A class that implements an unweighted, undirected graph
    using a dictionary as an adjacency list.
    """

    def __init__(self, adj_list=None):
        if adj_list is None:
            adj_list = {}
        if not isinstance(adj_list, dict):
            raise TypeError(
                f"Adjacent list must be a dict."
                f"Cannot initialize the graph with a {type(adj_list)}"
            )
        self.adj_list = adj_list

    def contains(self, vertex):
        return vertex in self.adj_list

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, va, vb):
        if not self.contains(va) or not self.contains(vb):
            raise ValueError(
                "One or both of the vertices provided"
                "are not present in the graph."
            )
        self.adj_list[va].append(vb)
        self.adj_list[vb].append(va)

    def get_vertices(self):
        return list(self.adj_list.keys())

    def get_edges(self):
        edges = []
        for vertex, adjacent in self.adj_list.items():
            for neighbor in adjacent:
                edge = [vertex, neighbor]
                edge.sort()
                if edge not in edges:
                    edges.append(edge)
        return edges

    def get_adjacency_list(self):
        return self.adj_list

    def bfs(self, start):
        if not self.contains(start):
            raise ValueError(
                "The vertex provided is not present in the graph."
            )
        distance = {start: 0}
        current = start
        q = Queue()
        q.push(current)
        while not q.empty():
            current = q.pop()
            dist = distance[current] + 1

            for neighbor in self.adj_list[current]:
                if neighbor not in distance:
                    q.push(neighbor)
                    distance[neighbor] = dist
        return distance

    def distance(self, start, target):
        if not self.contains(start) or not self.contains(target):
            raise ValueError(
                "One or both of the vertices provided"
                "are not present in the graph."
            )

        dist = -1

        if self.adj_list[start] == [] or self.adj_list[target] == []:
            return dist

        distances = self.bfs(start)

        if target not in distances:
            return dist

        return distances[target]

    def neighbors(self, vertex):
        if not self.contains(vertex):
            raise ValueError(
                "The vertex provided is not present in the graph."
            )
        return self.adj_list[vertex]
