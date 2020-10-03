import networkx as nx
from Position import Position

class Pawn:
    def __init__(self, pos, board):
        self.pos = pos
        self.g = board.g.copy()
        nx.set_node_attributes(self.g, False, 'win')
        for i in range(board.n):
            self.g.nodes[(0, i)]['win'] = True

    def movement(self, coord):
        self.pos = coord

    def get_position(self):
        return self.pos
