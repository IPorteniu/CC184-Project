import matplotlib.pyplot as plt
from UselfulObject import Algorithms
from Pawn import Pawn
from LogicBoard import BoardGame



board = BoardGame()
G = board.build_table()
player = Pawn((4, 0), (4, 4))
path = Algorithms.shortest_path(Algorithms,pawn=player, g=G)
print(path)
plt.show()



