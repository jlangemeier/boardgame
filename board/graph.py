class Vertex(object):
    """
    Vertex for a graph, can be connected to [0..n-1] other vertexes to form a
    graph.    Vertices are ID'd by a value supplied on initialization, and are
    initially unconnected nodes, with no additional properties.
    """

    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.properties = {}

    def __str__(self):
        id_str = str(self.id)
        adj_str = ', '.join([str(k) for k,v in self.adjacent.items()])
        return id_str + ' adjacent: ' + adj_str

    def add_neighbor(self, neighbor, weight=1):
        """
        Adds a neighbor to a vertex with a weight of 1, this way a non-weighted
        graph can be constructed without specifying any weight:
            self.add_neighbor(neighbor)
        """
        self.adjacent[neighbor] = weight

    def set_properties(self, **kwargs):
        """
        Sets multiple properties, each keyword argument is added to the properties
        dictionary based on rules for setting a single property value
        """
        for prop, value in kwargs.items():
            self.set_property(prop, value)

    def set_property(self, prop, value):
        """
        Sets a single property value, if the value exists, it's over written,
        if the value doesn't exist it is added.
        """
        self.properties[prop] = value

    def get_property(self, prop):
        """
        Returns a single property or None if the property isn't found
        """
        if prop in self.properties:
            return self.properties[prop]
        else:
            return None

    def get_connections(self):
        """
        Returns a list of keys in the adjacency dictionary, this should contain all
        ID's connected to a Vertex.
        """
        return list(self.adjacent.keys())

    def get_weight(self, neighbor):
        """
        Returns the weight of an edge between two Vertices, returns -1 for
        """
        return self.adjacent[neighbor]


class Graph(object):

    def __init__(self):
        self.vertices = {}
        self.size = 0

    def __iter__(self):
        return iter(self.vertices.values())

    def add_vertex(self, node):
        self.size += 1
        new_vertex = Vertex(node)
        self.vertices[node] = new_vertex
        return new_vertex

    def add_edge(self, frm, to, cost=1):
        if frm not in self.vertices:
            self.add_vertex(frm)
        if to not in self.vertices:
            self.add_vertex(to)

        self.vertices[frm].add_neighbor(to, cost)
        self.vertices[to].add_neighbor(frm, cost)

    def get_vertex(self, n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def get_vertices(self):
        return self.vertices.keys()


class Digraph(Graph):

    def __init__(self):
        super(Digraph, self).__init__()

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vertices:
            self.add_vertex(frm)

        self.vertices[frm].add_neighbor(to, cost)
