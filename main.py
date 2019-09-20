import pygame, visual as vis, buttons as but

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Fishing For Bass')
FPS = 60

while True:
    
    #Get Mouse Info
    (pressed_l, presed_m, pressed_r) = pygame.mouse.get_pressed()
    (mouse_x, mouse_y) = pygame.mouse.get_pos()     
    
    vis.shop_map()
    
    vis.start_game(mouse_x, mouse_y, pressed_l)
    
    vis.turn_stats(mouse_x, mouse_y, pressed_l, but.turn)
    
    pygame.display.update()
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()