import networkx as nx
import time as t

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

    # Funcion que permite seleccionar el algoritmo
    @staticmethod
    def algorithm_selector(g, pos, winning_nodes, n, identifier, paths):

        if identifier == 'up':
            StartDijkstra = t.time()
            for i in range(n):
                # TO - DO implementar algoritmo sin biblioteca

                paths.append(nx.dijkstra_path(g, pos, winning_nodes[i]))
            StopDijkstra = t.time()
            print("----------Dijkstra ejecucion promedio: ", (StopDijkstra-StartDijkstra)/n)

        elif identifier == 'down':
            StartAStar = t.time()
            for i in range(n):
                # TO - DO implementar algoritmo sin biblioteca
                paths.append(nx.astar_path(g, pos, winning_nodes[i]))
            StopAStar = t.time()
            print("----------A*Star ejecucion promedio: ", (StopAStar - StartAStar) / n)

        elif identifier == 'left':
            for i in range(n):
                # TO - DO implementar algoritmo sin biblioteca
                paths.append(nx.bellman_ford_path(g, pos, winning_nodes[i]))

        elif identifier == 'right':
            for i in range(n):
                # TO - DO implementar algoritmo sin biblioteca
                paths.append(nx.shortest_path(g, pos, winning_nodes[i]))
