import networkx as nx
from Position import Position
from UselfulObject import Algorithms
from BuildPawn import BuildPawn


class Pawn:
    def __init__(self, pos, board, identifier):
        self.pos = pos
        self.g = board.g.copy()
        self.n = board.n
        self.identifier = identifier
        BuildPawn.pawn_builder(self.g, identifier, self.n)

        # Se settean los nodos que son ganadores para el pawn
        self.winning_nodes = [n for n, d in self.g.nodes(data=True) if d['win']]

    def find_shortest(self):
        paths = []
        # Se usa dijkstra para conseguir los caminos desde self.pos hasta todos los winning_nodes
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

