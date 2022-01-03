from data_structures.queue import Queue


class Graph:
    """
    A class that implements an unweighted, undirected graph
    using a dictionary as an adjacency list.
    ...
    Methods
    _______
    contains(vertex):
        Returns True if the vertex is in the graph, false otherwise
    add_vertex(vertex):
        Adds the vertex to the graph if it doesn't exist yet
    add_edge(va, vb):
        Adds an edge connecting the vertices va and
        vb if both exist in the graph
    get_vertices():
        Returns a list of all the vertices in the graph
    get_edges():
        Returns a list of all the edges as pairs of vertices
    get_adjacency_list():
        Returns the entire graph as an adjacency list
    bfs(start):
        Does a breadth first traversal and returns the distance of each vertex
        from the start vertex
    distance(start, target):
        Returns the distance from the start vertex to the target vertex
    neighbors(vertex):
        Returns all the vertices with an edge connected to the given vertex
    """

    def __init__(self, adj_list=None):
        """
        Initialize the graph as empty, or with a given adjacency list
        :param adj_list: Dictionary containing vertices and their neighbors.
        """
        if adj_list is None:
            adj_list = {}
        if not isinstance(adj_list, dict):
            raise TypeError(
                f"Adjacent list must be a dict."
                f"Cannot initialize the graph with a {type(adj_list)}"
            )
        self.adj_list = adj_list

    def contains(self, vertex):
        """
        Checks if the given vertex is in the graph
        :param vertex: Vertex to check
        :return: True if the vertex is in the graph, false otherwise
        """
        return vertex in self.adj_list

    def add_vertex(self, vertex):
        """
        Adds the vertex to the graph if it doesn't exist yet
        :param vertex: New vertex to add to the list
        """
        if not self.contains(vertex):
            self.adj_list[vertex] = []

    def add_edge(self, va, vb):
        """
        Adds an edge connecting the vertices va and
        vb if both exist in the graph
        :param va: Vertex at one end of the edge
        :param vb: Vertex at the other end of the edge
        """
        if not self.contains(va) or not self.contains(vb):
            raise ValueError(
                "One or both of the vertices provided"
                "are not present in the graph."
            )
        self.adj_list[va].append(vb)
        self.adj_list[vb].append(va)

    def get_vertices(self):
        """
        Returns a list of all the vertices in the graph
        :return: List containing every vertebrate in the graph
        """
        return list(self.adj_list.keys())

    def get_edges(self):
        """
        Returns a list of all the edges as pairs of vertices
        :return: List containing every edge as a pair of vertices
        """
        edges = []
        for vertex, adjacent in self.adj_list.items():
            for neighbor in adjacent:
                edge = [vertex, neighbor]
                edge.sort()
                if edge not in edges:
                    edges.append(edge)
        return edges

    def get_adjacency_list(self):
        """
        Returns the entire graph as an adjacency list
        :return: Adjacency list representation of the graph
        """
        return self.adj_list

    def bfs(self, start):
        """
        Does a breadth first traversal and returns the distance of each vertex
        from the start vertex
        :param start: Vertex as the root of the traversal
        :return: Dictionary containing every connected vertex
            and their distances from the starting vertex
        """
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

            for neighbor in self.neighbors(current):
                if neighbor not in distance:
                    q.push(neighbor)
                    distance[neighbor] = dist
        return distance

    def distance(self, start, target):
        """
        Returns the distance from the start vertex to the target vertex
        :param start: Vertex for the root of the traversal
        :param target: Vertex to get the distance of
        :return: Number of edges from start to target, -1 if not connected
        """
        if not self.contains(start) or not self.contains(target):
            raise ValueError(
                "One or both of the vertices provided"
                "are not present in the graph."
            )

        dist = -1

        if self.neighbors(start) == [] or self.neighbors(target) == []:
            return dist

        distances = self.bfs(start)

        if target not in distances:
            return dist

        return distances[target]

    def neighbors(self, vertex):
        """
        Returns all the vertices with an edge connected to the given vertex
        :param vertex: Vertex to get neighbors of
        :return: All neighbors of the given vertex
        """
        if not self.contains(vertex):
            raise ValueError(
                "The vertex provided is not present in the graph."
            )
        return self.adj_list[vertex]
