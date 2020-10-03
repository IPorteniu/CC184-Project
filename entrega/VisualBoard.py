import pygame
from pygame.locals import *
import sys
import math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class visualBoard:
    def __init__(self, board):
        self.board = board
        self.game_over = False

    def draw_board(self):
        COLUMN_COUNT = self.board.n
        ROW_COUNT = self.board.n
        SQUARESIZE = 100
        RADIUS = 10

        screen = pygame.display.set_mode((1080, 720))

        for c in range(self.board.n):
            for r in range(9):
                pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
                pygame.draw.circle(screen, BLACK, (int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

        pygame.display.update()

    def start_game(self):

        pygame.init()
        window_surface = pygame.display.set_mode((1080, 720), 0, 32)
        pygame.display.set_caption('Quoridor')

        # Colors

        pygame.display.update()
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            self.draw_board()
            if self.game_over:
                pygame.time.wait(3000)
