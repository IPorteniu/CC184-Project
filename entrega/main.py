import matplotlib.pyplot as plt
from Pawn import Pawn
from LogicBoard import BoardGame
from VisualBoard import visualBoard
import sys

game_over = False

board = BoardGame()
player1 = Pawn((4, 8), board, 'up')
player2 = Pawn((4, 0), board, 'down')
player3 = Pawn((8, 4), board, 'right')
player4 = Pawn((0, 4), board, 'left')
# visual = visualBoard(board)
# Profesor, le debo la parte visual del juego
# visual.start_game()
while not game_over:
    player1.movement()
    player2.movement()
    #player3.movement()
    #player4.movement()


