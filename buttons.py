import pygame

pygame.init()


def start_button(x, y, left):
    if ((800 < x < 880) and (435 < y < 465) and (left > 0)):
        return 1
    else:
        return 0


