import matplotlib.pyplot as plt
from UselfulObject import Algorithms
from Pawn import Pawn
from LogicBoard import BoardGame


board = BoardGame()
player = Pawn((4, 0), board)
path = Algorithms.shortest_path(pawn=player, g=board.g)
print(path)
plt.show()



