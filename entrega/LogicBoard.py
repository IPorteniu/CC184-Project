import networkx as nx


class BoardGame:
    def __init__(self):
        self.n = 9
        self.g = nx.grid_2d_graph(self.n, self.n)
        nx.set_node_attributes(self.g, False, 'win')
        nx.set_node_attributes(self.g, False, 'occupied')
        # Para el futuro se puede añadir atributos a los edges para no dejar que los pawns pasen por ese edge
        # TO-DO nx.set_edge_attributes(self.g,False,'walkable')
        # Acceder a los valores ( key:value ) del dict de los nodos para
        # Comprobar antes de caminar a un nodo si puedes pasar por esa arista :D
        pos = dict((p, p) for p in self.g.nodes())
        labels = dict(((i, j), i + (self.n - 1 - j) * self.n) for i, j in self.g.nodes())
        nx.draw_networkx(self.g, pos=pos, labels=labels)
