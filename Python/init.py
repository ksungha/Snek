import pygame
import libraries
from libraries import *

# initailize game
pygame.init()

# initialze window
pygame.display.set_caption("Snake in Python")
game_window = pygame.display.set_mode((win_x, win_y))

# FPS
fps = pygame.time.Clock()
