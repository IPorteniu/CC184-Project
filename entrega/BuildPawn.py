import networkx as nx


class BuildPawn:
    def __init__(self):
        pass

    @staticmethod
    def pawn_builder(g, identifier, n):
        nx.set_node_attributes(g, False, 'win')

        if identifier == 'up':
            for i in range(n):
                g.nodes[(i, 0)]['win'] = True

        elif identifier == 'down':
            for i in range(n):
                g.nodes[(i, 8)]['win'] = True

        elif identifier == 'left':
            for i in range(n):
                g.nodes[(8, i)]['win'] = True

        elif identifier == 'right':
            for i in range(n):
                g.nodes[(0, i)]['win'] = True
