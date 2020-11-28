import sys
import networkx as nx
from LogicPawnFactory import BuildPawn


class Pawn:
    def __init__(self, start_position, board, identifier, walls):
        self.pos = start_position
        self.g = board.g.copy()
        self.n = board.n
        self.identifier = identifier
        self.free_spaces = board.g
        self.num_walls = int(walls)
        self.movement_history = []
        self.path = []
        self.shortest = 0
        BuildPawn.pawn_builder(self.g, identifier, self.n)
        # Se settean los nodos que son ganadores para el pawn
        self.winning_nodes = [n for n, d in self.g.nodes(data=True) if d['win']]

    def find_shortest(self):
        paths = []

        # Se usa la funcion algorithm selector para cambiar de algoritmo segun su identifier
        BuildPawn.algorithm_selector(self.free_spaces, self.pos, self.winning_nodes, self.n, self.identifier, paths)

        # Setteo dos variables que me ayuden a encontrar el camino mas corto
        shortest = len(paths[0])
        pos = 0
        for i in range(1, self.n):
            if len(paths[i]) < shortest:
                pos = i
                shortest = len(paths[i])

        paths[pos].pop(0)
        return paths[pos]

    def is_a_winner(self):
        if self.pos not in self.winning_nodes:
            return
        print("\n¡¡Ganaste!! Jugador con identificador: ", self.identifier)
        print("Historial de movimientos: ",self.movement_history)
        sys.exit()

    def movement(self):
        print("\nTurno de " + str(self.identifier))
        self.push_location()
        self.path = self.find_shortest()
        self.shortest = int(len(self.path))
        if not self.free_spaces.nodes[self.path[0]]['occupied']:
            print(self.identifier + " se mueve a" + str(self.path[0]))
            self.move_forward()
            self.is_a_winner()
        else:
            print("\n Oops, la casilla " + str(self.path[0]) + " se encuentra ocupada")
            self.next_was_occupied()
            self.is_a_winner()

    def move_forward(self):
        self.free_spaces.nodes[self.pos]['occupied'] = False
        self.pos = self.path[0]
        self.free_spaces.nodes[self.path[0]]['occupied'] = True

    def next_was_occupied(self):
        print("¡" + self.identifier + " salta a " + str(self.path[1])+"!")
        self.free_spaces.nodes[self.pos]['occupied'] = False
        self.path.pop(0)
        self.free_spaces.nodes[self.path[0]]['occupied'] = True
        self.pos = self.path[0]

    def push_location(self):
        self.movement_history.append(self.pos)

    def use_wall(self, nodes):
        self.num_walls -= 2
        if self.num_walls > 0:
            self.free_spaces.remove_edge(nodes[0], nodes[1])

    def get_path(self):
        return self.path
