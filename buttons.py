import pygame

pygame.init()

turn = 1
turn_ended = 0
ai_done = False

def start_button(x, y, left):
    if ((800 < x < 880) and (435 < y < 465) and (left > 0)):
        return 1
    else:
        return 0

def end_button(x, y, left):
    global turn_ended
    global turn
    if turn_ended < turn:
        if (20 < x < 100) and (700 < y < 730) and (left > 0):
            turn_ended += 1
    elif turn_ended == turn and ai_done == True:
            turn += 1