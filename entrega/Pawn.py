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

        # Se usa la funcion algorithm selector para cambiar de algoritmo segun su identifier
        BuildPawn.algorithm_selector(self.g, self.pos, self.winning_nodes, self.n, self.identifier, paths)

        # Setteo dos variables que me ayuden a encontrar el camino mas corto
        min = len(paths[0])
        pos = 0
        for i in range(1, self.n):
            if len(paths[i]) < min:
                pos = i
                min = len(paths[i])

        # Elimino el primero ya que es mi posicion actual
        paths[pos].pop(0)
        return paths[pos]

    def is_a_winner(self):
        print("ganaste ctmr ", self.identifier)
        return

    def movement(self):
        path = self.find_shortest()
        # Hacemos validacion de si ya esta en la casilla ganadora
        if len(path) == 0:
            self.is_a_winner()
            return
        self.pos = path[0]
        path.pop(0)
        print(path)
