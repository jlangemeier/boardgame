from collections import namedtuple
from math import floor

from . import graph

Point = namedtuple('Point', ['row','column'])
# Axial and Cube are related in that s + q + r = 0,
# so it follows that -s = q + r
# to save space, Axial can be used in most cases for hex coordinates
Axial = namedtuple('Axial', ['q','r'])
Cube = namedtuple('Cube', ['q','r','s'])


class Board(object):

    def __init__(self, height, width):
        self.height = height
        self.width = width

        self.board = graph.Digraph()

    def get_edges(self, location):
        vertex = self.board.get_vertex(location)

        return vertex.get_connections()


class SquareBoard(Board):

    def __init__(self, height, width):
        super(SquareBoard, self).__init__(height, width)

        self.initialize_board()

    def initialize_board(self):
        # Everything gets the same default weight to begin with
        weight = 1

        # Add all vertices
        for row in range(self.height):
            for col in range(self.width):
                self.board.add_vertex(Point(row,col))

        # Add edges - no wrapping
        #     0,0                = top, left corner
        #     height-1,width-1 = bottom, right corner
        for vertex in self.board:
            vertex_id = vertex.id
            row, col = vertex_id
            # Add left edge
            if col > 0:
                self.board.add_edge(vertex_id, Point(row, col-1), weight)
            # Add right edge
            if col < (self.width - 1):
                self.board.add_edge(vertex_id, Point(row, col+1), weight)
            # Add top edge
            if row > 0:
                self.board.add_edge(vertex_id, Point(row-1, col), weight)
            # Add bottom edge
            if row < (self.height - 1):
                self.board.add_edge(vertex_id, Point(row+1, col), weight)


class HexBoard(Board):

    def __init__(self, height, width):
        super(HexBoard, self).__init__(height, width)

        self.initialize_board()

    def initialize_board(self):
        # Everything gets the same default weight to begin with
        weight = 1

        # Add all vertices
        for r in range(self.height):
            offset = int(floor(r/2.0))
            for q in range(-offset, self.width-offset):
                self.board.add_vertex(Axial(q, r))

        # Add Edges
        # Pointy topped Hexagons
        for vertex in self.board:
            vertex_id = vertex.get_id()
            q, r = vertex_id

            # North-West Edge
            if self.board.get_vertex(Axial(q,r-1)):
                self.board.add_edge(vertex_id, Axial(q,r-1), weight)
            # North-East Edge
            if self.board.get_vertex(Axial(q+1,r-1)):
                self.board.add_edge(vertex_id, Axial(q+1,r-1), weight)
            # East Edge
            if self.baord.get_vertex(Axial(q+1,r)):
                self.board.add_edge(vertex_id, Axial(q+1,r), weight)
            # South-East Edge
            if self.baord.get_vertex(Axial(q,r+1)):
                self.board.add_edge(vertex_id, Axial(q+1,r), weight)
            # South-West Edge
            if self.baord.get_vertex(Axial(q-1,r+1)):
                self.board.add_edge(vertex_id, Axial(q-1,r+1), weight)
            # West Edge
            if self.baord.get_vertex(Axial(q-1,r)):
                self.board.add_edge(vertex_id, Axial(q-1,r), weight)
