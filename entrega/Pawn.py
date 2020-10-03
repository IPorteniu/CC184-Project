import networkx as nx
from Position import Position


class Pawn:
    def __init__(self, pos, board):
        self.pos = pos
        self.g = board.g.copy()
        nx.set_node_attributes(self.g, False, 'win')
        for i in range(board.n):
            self.g.nodes[(0, i)]['win'] = True
        self.winning_nodes = [n for n, d in self.g.nodes(data=True) if d['win']]
        self.movement()

    def movement(self):
        paths = []
        for i in range(len(self.winning_nodes)-1):
            paths = [list(Algorithms.shortest_path(self, self.winning_nodes[i]))]
            print(paths[i])
        shortest = min(len(paths))
        #print(shortest)

    def get_position(self):
        return self.pos
