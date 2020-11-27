from LogicBoardFactory import BoardGame
from Pawn import Pawn
import networkx as nx


class Game:
    def __init__(self, num_players):
        self.num_players = num_players
        self.num_walls = 20
        self.player1 = None
        self.player2 = None
        self.player3 = None
        self.player4 = None
        self.board = None

    def startgame(self):
        game_over = False

        self.board = BoardGame()
        if self.num_players == 4:
            self.player1 = Pawn((4, 8), self.board, 'up', self.num_walls / self.num_players)
            self.player2 = Pawn((4, 0), self.board, 'down', self.num_walls / self.num_players)
            self.player3 = Pawn((8, 4), self.board, 'right', self.num_walls / self.num_players)
            self.player4 = Pawn((0, 4), self.board, 'left', self.num_walls / self.num_players)
            while not game_over:
                self.player1.movement()
                self.player2.movement()
                self.player3.movement()
                self.player4.movement()

        self.player1 = Pawn((4, 8), self.board, 'up', self.num_walls / self.num_players)
        self.player2 = Pawn((4, 0), self.board, 'down', self.num_walls / self.num_players)
        erase = [(4,4),(4,5),(4,6)]
        #self.player2.use_wall(erase)
        print(self.player2.num_walls)
        while not game_over:
            self.player1.movement()
            self.player2.movement()

    def put_wall(self, bully, sheep1, sheep2, sheep3, nodes):
        dummy_board = self.board.copy()

        if nx.has_path(board, bully.pos, [e for e in sheep1.winning_nodes]):
            print(str(sheep1.identifier) + " tiene camino")
