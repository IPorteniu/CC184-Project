from LogicBoardFactory import BoardGame
from Pawn import Pawn


class Game:
    def __init__(self, num_players):
        self.num_players = num_players
        self.num_walls = 20

    def startgame(self):
        game_over = False

        board = BoardGame()
        if self.num_players == 4:
            player1 = Pawn((4, 8), board, 'up', self.num_walls / self.num_players)
            player2 = Pawn((4, 0), board, 'down', self.num_walls / self.num_players)
            player3 = Pawn((8, 4), board, 'right', self.num_walls / self.num_players)
            player4 = Pawn((0, 4), board, 'left', self.num_walls / self.num_players)
            while not game_over:
                player1.movement()
                player2.movement()
                player3.movement()
                player4.movement()

        player1 = Pawn((4, 8), board, 'up', self.num_walls / self.num_players)
        player2 = Pawn((4, 0), board, 'down', self.num_walls / self.num_players)
        while not game_over:
            player1.movement()
            player2.movement()
