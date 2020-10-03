import matplotlib.pyplot as plt
from Pawn import Pawn
from LogicBoard import BoardGame


board = BoardGame()
player = Pawn((4, 8), board, 'down')
player.movement()
plt.show()