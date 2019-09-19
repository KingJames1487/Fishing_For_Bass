import pygame, intro, dimensions as dim

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Fishing For Bass')
screen = pygame.display.set_mode((dim.width, dim.height))
FPS = 60

turn = 0

while True:
    
    #Get Mouse Info
    (pressed_l, presed_m, pressed_r) = pygame.mouse.get_pressed()
    (mouse_x, mouse_y) = pygame.mouse.get_pos()     
    
    intro.shop_map()
    
    intro.start_game(mouse_x, mouse_y, pressed_l)
    
    pygame.display.update()
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()