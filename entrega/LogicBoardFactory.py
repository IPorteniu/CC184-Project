import networkx as nx


class BoardGame:
    def __init__(self):
        self.n = 9
        self.g = nx.grid_2d_graph(self.n, self.n)

        # Usaremos un atributo para decidir que nodos le permiten ganar a los pawns
        nx.set_node_attributes(self.g, False, 'win')

        # Usaremos una tributo occupied para saber si el pawn puede pararse en esa posicion
        nx.set_node_attributes(self.g, False, 'occupied')
        # Usaremos un atributo 'walkable' para poder decidir por donde se puede ir

        # pos = dict((p, p) for p in self.g.nodes())
        # labels = dict(((i, j), i + (self.n - 1 - j) * self.n) for i, j in self.g.nodes())
        # nx.draw_networkx(self.g, pos=pos, labels=labels)
