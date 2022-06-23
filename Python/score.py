from cmath import rect
from init import *
score = 0


def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render("Score: " + True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)
