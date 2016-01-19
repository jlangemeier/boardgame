import unittest
from board import graph

class TestVertex(unittest.TestCase):

    def setUp(self):
        self.default_vertex = graph.Vertex('a')

    def tearDown(self):
        self.default_vertex.id = None
        self.default_vertex.adjacent = None
        self.default_vertex.properties = None
        self.default_vertex = None

    def test_string_output(self):
        self.default_vertex.add_neighbor('b', 10)
        vertices = ', '.join(self.default_vertex.get_connections())
        output = self.default_vertex.id + ' adjacent: ' + vertices

        self.assertEqual(output, self.default_vertex.__str__())

    def test_default_adjacency_empty(self):
        error = "Initialization Failed - Adjacency dictionary contains data"
        length = len(self.default_vertex.adjacent.keys())

        self.assertEqual(length, 0, error)

    def test_add_neighbor(self):
        key_missing = "Key not correctly added"
        value_missing = "Value was not correctly assigned to the key"
        self.default_vertex.add_neighbor('b', 10)

        self.assertTrue('b' in self.default_vertex.get_connections(), key_missing)
        self.assertEqual(self.default_vertex.get_weight('b'), 10, value_missing)

    def test_set_property(self):
        key_missing = "No key was found in the properties dictionary"
        value_missing = "Value was not correctly assigned to the key"
        self.default_vertex.set_property('string', 'AB')

        self.assertTrue('string' in self.default_vertex.properties, key_missing)
        self.assertEqual(self.default_vertex.get_property('string'), 'AB', value_missing)

    def test_update_property(self):
        value_wrong = "Value was not updated"
        self.default_vertex.set_property('string', 'AB')
        self.default_vertex.set_property('string', 'DE')

        self.assertEqual(self.default_vertex.get_property('string'), 'DE', value_wrong)

    def test_set_properties(self):
        key_missing = "Key '{}' not found in the properties dictionary"
        value_missing = "Key '{}' doesn't have Value '{}'"
        self.default_vertex.set_properties(string='AB', integer=10)

        properties = self.default_vertex.properties
        self.assertTrue('string' in properties, key_missing.format('string'))
        self.assertTrue('integer' in properties, key_missing.format('integer'))

        string = self.default_vertex.get_property('string')
        integer = self.default_vertex.get_property('integer')
        self.assertEqual(string, 'AB', value_missing.format('string','AB'))
        self.assertEqual(string, 'AB', value_missing.format('integer', 10))


class TestGraph(unittest.TestCase):

    def setUp(self):
        self.default_graph = graph.Graph()
        self.vertex_list = ['a', 'b', 'c', 'd', 'e', 'f']

    def tearDown(self):
        self.default_graph.vertices = None
        self.default_graph.size = 0
        self.default_graph = None

    # Shared Methods
    def add_vertices(self):
        for node in self.vertex_list:
            self.default_graph.add_vertex(node)

    # Test Runners
    def test_default_graph(self):
        size_error = "Default size should be 0"
        length = len(self.default_graph.get_vertices())

        self.assertEqual(self.default_graph.size, 0, size_error)
        self.assertEqual(length, 0, size_error)

    def test_add_vertices(self):
        size_error = "Reported Size {}, Total Vertices {}"

        self.add_vertices()
        self_size = self.default_graph.size
        expected_size = len(self.default_graph.get_vertices())

        self.assertEqual(
            self_size,
            expected_size,
            size_error.format(self_size, expected_size)
        )

    def test_add_edges(self):
        num_edge_error = "Number of edges for Vertex '{}' = {}, expected 2"

        self.add_vertices()
        self.default_graph.add_edge(self.vertex_list[0], self.vertex_list[1])
        self.default_graph.add_edge(self.vertex_list[0], self.vertex_list[2])

        vertex = self.default_graph.get_vertex(self.vertex_list[0])
        edges = vertex.get_connections()

        self.assertEqual(
            sorted(self.vertex_list[1:3]),
            sorted(edges),
            num_edge_error.format(vertex.id, len(edges))
        )

    def test_default_edge_weight(self):
        default_error = "Weight defaults to 1, was set to {}"

        self.add_vertices()
        self.default_graph.add_edge(self.vertex_list[0], self.vertex_list[1])

        vertex = self.default_graph.get_vertex(self.vertex_list[0])

        self.assertEqual(
            vertex.get_weight(self.vertex_list[1]),
            1,
            default_error.format(vertex.get_weight(self.vertex_list[1]))
        )

    def test_set_edge_weights(self):
        weight_error = "Weight Expected {}, Weight Returned {}"

        weight = 2
        self.add_vertices()
        self.default_graph.add_edge(self.vertex_list[0], self.vertex_list[1], weight)

        vertex_0 = self.default_graph.get_vertex(self.vertex_list[0])
        vertex_1 = self.default_graph.get_vertex(self.vertex_list[1])

        self.assertEqual(
            vertex_0.get_weight(self.vertex_list[1]),
            weight,
            weight_error.format(vertex_0.get_weight(self.vertex_list[1]), weight)
        )

        self.assertEqual(
            vertex_1.get_weight(self.vertex_list[0]),
            weight,
            weight_error.format(vertex_1.get_weight(self.vertex_list[0]), weight)
        )


class TestDigraph(unittest.TestCase):

    def setUp(self):
        self.default_graph = graph.Digraph()
        self.vertex_list = ['a', 'b', 'c', 'd']

    def tearDown(self):
        self.default_graph.vertices = None
        self.default_graph.size = 0
        self.default_graph = None

    # Shared Methods
    def add_vertices(self):
        for node in self.vertex_list:
            self.default_graph.add_vertex(node)

    # Test Runners
    def test_add_edges(self):
        num_edge_error = "Number of edges for Vertex '{}' = {}, expected {}"

        self.add_vertices()
        self.default_graph.add_edge(self.vertex_list[0], self.vertex_list[1])
        self.default_graph.add_edge(self.vertex_list[0], self.vertex_list[2])

        vertex_0 = self.default_graph.get_vertex(self.vertex_list[0])
        vertex_1 = self.default_graph.get_vertex(self.vertex_list[1])
        edges_0 = vertex_0.get_connections()
        edges_1 = vertex_1.get_connections()
        self.assertEqual(
            sorted(self.vertex_list[1:3]),
            sorted(edges_0),
            num_edge_error.format(vertex_0.id, len(edges_0), 2)
        )

        self.assertEqual(
            len(edges_1),
            0,
            num_edge_error.format(vertex_1.id, len(edges_1), 0)
        )

if __name__ == '__main__':
    unittest.main()
