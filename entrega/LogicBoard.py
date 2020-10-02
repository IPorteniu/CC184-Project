import networkx as nx

class BoardGame:
    def __init__(self):
        pass

    def build_table(self):

        # Grafo 2D de 9x9
        N = 9
        g = nx.grid_2d_graph(N, N)
        pos = dict((p, p) for p in g.nodes())
        labels = dict(((i, j), i + (N - 1 - j) * N) for i, j in g.nodes())
        nx.draw_networkx(g, pos=pos, labels=labels)
        return g