# Para el movimiento del jugador se quiere usar los eventos de pygame
from Position import Position

class Pawn:
    def __init__(self, pos, goal):
        self.pos = pos
        self.goal = goal

    def movement(self, coord):
        self.pos = coord

    def get_position(self):
        return self.pos
