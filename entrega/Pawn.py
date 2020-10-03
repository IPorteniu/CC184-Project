import networkx as nx
from Position import Position
from UselfulObject import Algorithms


class Pawn:
    def __init__(self, pos, board):
        self.pos = pos
        self.g = board.g.copy()
        self.n = board.n
        nx.set_node_attributes(self.g, False, 'win')
        for i in range(board.n):
            self.g.nodes[(i, 0)]['win'] = True
        self.winning_nodes = [n for n, d in self.g.nodes(data=True) if d['win']]

    def get_position(self):
        return self.pos

    def find_shortest(self):
        paths = []
        for i in range(self.n):
            paths.append(nx.dijkstra_path(self.g, self.pos, self.winning_nodes[i]))
        min = len(paths[0])
        pos = 0
        for i in range(1, self.n):
            if len(paths[i]) < min:
                pos = i
                min = len(paths[i])
        paths[pos].pop(0)
        return paths[pos]

    def movement(self):
        path = self.find_shortest()
        self.pos = path[0]
        path.pop(0)
