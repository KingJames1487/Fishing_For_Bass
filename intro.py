import pygame, colour as col, dimensions as dim, buttons as but

screen = pygame.display.set_mode((dim.width, dim.height))
game_start = 0


def text(text, colour, x, y, size):
    font = pygame.font.Font('freesansbold.ttf', size)
    text = font.render(text, True, colour)
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)
    
    
def line(colour, from_x, from_y, to_x, to_y, thick):
    pygame.draw.line(screen, colour, [from_x, from_y], [to_x, to_y], thick)
    
    
def rect(colour, x, y, width, height):
    pygame.draw.rect(screen, colour, [x, y, width, height])


def pic(location, w, h, x, y):
    image = pygame.image.load(location)
    image = pygame.transform.scale(image, (w, h))
    rect = image.get_rect()
    rect = rect.move((x, y))
    screen.blit(image, rect)

def shop_map():
    #Map
    screen.fill(col.BROWN)
    pic('risk.jpg', dim.width - dim.shop_width - 20, dim.height - 20, 10, 10)
    rect(col.BLACK, dim.width - dim.shop_width, 0, dim.shop_width, dim.height)
    rect(col.DARK_BROWN, dim.width - 240, 10, 230, dim.height - 20)
    
    #Totals
    rect(col.BLACK, dim.shop_column_1 - 27, 18, 204, 54)
    rect(col.LIGHT_GRAY, dim.shop_column_1 - 25, 20, dim.shop_box_w * 4, dim.shop_box_h)
    
    #Food Per Turn
    rect(col.BLACK, dim.shop_column_1 - 17, 78, 84, 54)
    rect(col.YELLOW, dim.shop_column_1 - 15, 80, dim.per_turn_w, dim.per_turn_h)

    #Wood Per Turn
    rect(col.BLACK, dim.shop_column_2 - 17, 78, 84, 54)
    rect(col.BROWN, dim.shop_column_2 - 15, 80, dim.per_turn_w, dim.per_turn_h)
    
    #Steel Per Turn
    rect(col.BLACK, dim.shop_column_1 - 17, 138, 84, 54)
    rect(col.STEEL, dim.shop_column_1 - 15, 140, dim.per_turn_w, dim.per_turn_h)
    
    #Food Per Turn
    rect(col.BLACK, dim.shop_column_2 - 17, 138, 84, 54)
    rect(col.OIL, dim.shop_column_2 - 15, 140, dim.per_turn_w, dim.per_turn_h)
    
    
    #Turn Marker
    rect(col.BLACK, dim.shop_column_1 - 27, 218, 104, 54)
    rect(col.LIGHT_GRAY, dim.shop_column_1 - 25, 220, dim.shop_box_w * 2, dim.shop_box_h)
    text('Turn:', col.BLACK, dim.shop_column_1 + 25, 245, 16)
    rect(col.BLACK, dim.shop_column_2 - 2, 218, 54, 54)
    rect(col.WHITE, dim.shop_column_2, 220, dim.shop_box_w, dim.shop_box_h)
    
    #On Deck Marker
    rect(col.BLACK, dim.shop_column_1 - 27, 288, 104, 54)
    rect(col.LIGHT_GRAY, dim.shop_column_1 - 25, 290, dim.shop_box_w * 2, dim.shop_box_h)
    text('Place Unit:', col.BLACK, dim.shop_column_1 + 25, 315, 16)
    rect(col.BLACK, dim.shop_column_2 - 2, 288, 54, 54)
    rect(col.BROWN, dim.shop_column_2, 290, dim.shop_box_w, dim.shop_box_h)
    
    line(col.BLACK, dim.width - 240, 365, dim.width, 365, 10)
    
    #Shop Markers
    rect(col.BLACK, dim.shop_column_1 - 2, dim.shop_row_5 - 2, 54, 54)
    rect(col.BLACK, dim.shop_column_1 - 2, dim.shop_row_4 - 2, 54, 54)
    rect(col.BLACK, dim.shop_column_1 - 2, dim.shop_row_3 - 2, 54, 54)
    rect(col.BLACK, dim.shop_column_1 - 2, dim.shop_row_2 - 2, 54, 54)
    rect(col.BLACK, dim.shop_column_1 - 2, dim.shop_row_1 - 2, 54, 54)
    rect(col.BLACK, dim.shop_column_2 - 2, dim.shop_row_5 - 2, 54, 54)
    rect(col.BLACK, dim.shop_column_2 - 2, dim.shop_row_4 - 2, 54, 54)
    rect(col.BLACK, dim.shop_column_2 - 2, dim.shop_row_3 - 2, 54, 54)
    rect(col.BLACK, dim.shop_column_2 - 2, dim.shop_row_2 - 2, 54, 54)
    rect(col.BLACK, dim.shop_column_2 - 2, dim.shop_row_1 - 2, 54, 54)
    rect(col.BROWN, dim.shop_column_1, dim.shop_row_5, dim.shop_box_w, dim.shop_box_h)
    rect(col.BROWN, dim.shop_column_1, dim.shop_row_4, dim.shop_box_w, dim.shop_box_h)
    rect(col.BROWN, dim.shop_column_1, dim.shop_row_3, dim.shop_box_w, dim.shop_box_h)
    rect(col.BROWN, dim.shop_column_1, dim.shop_row_2, dim.shop_box_w, dim.shop_box_h)
    rect(col.BROWN, dim.shop_column_1, dim.shop_row_1, dim.shop_box_w, dim.shop_box_h)
    rect(col.BROWN, dim.shop_column_2, dim.shop_row_5, dim.shop_box_w, dim.shop_box_h)
    rect(col.BROWN, dim.shop_column_2, dim.shop_row_4, dim.shop_box_w, dim.shop_box_h)
    rect(col.BROWN, dim.shop_column_2, dim.shop_row_3, dim.shop_box_w, dim.shop_box_h)
    rect(col.BROWN, dim.shop_column_2, dim.shop_row_2, dim.shop_box_w, dim.shop_box_h)
    rect(col.BROWN, dim.shop_column_2, dim.shop_row_1, dim.shop_box_w, dim.shop_box_h)
    

def start_screen():
    rect(col.DARK_BROWN, dim.map_center - 300, 250, 600, 250)
    rect(col.RED, dim.map_center - 280, 270, 560, 210)
    rect(col.DARK_BROWN, dim.map_center - 275, 275, 550, 200)
    text('Fishing For Bass', col.BLACK, dim.map_center, dim.height / 2, 50)

    
def start_menu():
    rect(col.BLACK, dim.map_center + 175, 435, 80, 30)
    rect(col.RED, dim.map_center + 178, 438, 74, 24)
    text('Click to Start', col.BLACK, dim.map_center + 215, 450, 10)


def start_game(x, y, left):        
    global game_start
    if game_start > 0:
        None
    elif but.start_button(x, y, left) > 0:
        game_start = 1    
    else:
        start_screen()
        start_menu()
