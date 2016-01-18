import unittest
from board import board


class TestSquareBoard(unittest.TestCase):

    def setUp(self):
        height, width = 8, 8
        self.test_board = board.SquareBoard(height, width)

    def tearDown(self):
        self.test_board = None

    def test_corner_node(self):
        weight_error = 'Initialized Weight != 1'
        location_error = 'Adjacent nodes are different than expected'
        neighbor_error = 'Number of adjacent nodes is different than expected'

        adj_weight = 1
        location =  (0,0)
        adj_right = (0,1)
        adj_below = (1,0)

        self.assertEqual(len(self.test_board.get_edges(location)), 2, neighbor_error)
        for vertex in self.test_board.get_edges(location):
            weight = self.test_board.board.get_vertex(location).get_weight(vertex)
            if vertex[0] == adj_right[0] and vertex[1] == adj_right[1]:
                self.assertEqual(vertex[0], adj_right[0], location_error)
                self.assertEqual(vertex[1], adj_right[1], location_error)
                self.assertEqual(weight, adj_weight, weight_error)
            elif vertex[0] == adj_below[0] and vertex[1] == adj_below[1]:
                self.assertEqual(vertex[0], adj_below[0], location_error)
                self.assertEqual(vertex[1], adj_below[1], location_error)
                self.assertEqual(weight, adj_weight, weight_error)

    def test_interior_node(self):
        weight_error = 'Initialized Weight != 1'
        location_error = 'Adjacent nodes are different than expected'
        neighbor_error = 'Number of adjacent nodes is different than expected'

        adj_weight = 1
        location =  (2,2)
        adj_right = (2,3)
        adj_left  = (2,1)
        adj_below = (3,2)
        adj_above = (1,2)

        self.assertEqual(len(self.test_board.get_edges(location)), 4, neighbor_error)
        for vertex in self.test_board.get_edges(location):
            weight = self.test_board.board.get_vertex(location).get_weight(vertex)
            if vertex[0] == adj_right[0] and vertex[1] == adj_right[1]:
                self.assertEqual(vertex[0], adj_right[0], location_error)
                self.assertEqual(vertex[1], adj_right[1], location_error)
                self.assertEqual(weight, adj_weight, weight_error)
            elif vertex[0] == adj_left[0] and vertex[1] == adj_left[1]:
                self.assertEqual(vertex[0], adj_left[0], location_error)
                self.assertEqual(vertex[1], adj_left[1], location_error)
                self.assertEqual(weight, adj_weight, weight_error)
            elif vertex[0] == adj_below[0] and vertex[1] == adj_below[1]:
                self.assertEqual(vertex[0], adj_below[0], location_error)
                self.assertEqual(vertex[1], adj_below[1], location_error)
                self.assertEqual(weight, adj_weight, weight_error)
            elif vertex[0] == adj_above[0] and vertex[1] == adj_above[1]:
                self.assertEqual(vertex[0], adj_above[0], location_error)
                self.assertEqual(vertex[1], adj_above[1], location_error)
                self.assertEqual(weight, adj_weight, weight_error)


if __name__ == '__main__':
    unittest.main()
