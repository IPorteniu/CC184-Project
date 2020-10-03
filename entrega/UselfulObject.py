import networkx as nx
from Pawn import Pawn


class Algorithms:
    def __init__(self):
        pass

    def put_wall(pawn, wall, board):
        # En esta función se planea usar nx.has.path()
        return True

    @staticmethod
    def shortest_path(pawn=Pawn, g=[]):
        # En este caso usaremos el algoritmo de dijkstra proporcionado por la Biblioteca Networkx
        path = nx.shortest_path(g, pawn.pos)
        return path

    def a_star_algorithm(self, pawn, board):
        # Se planea utilizar nx.astar_path()
        return True
