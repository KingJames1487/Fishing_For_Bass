import pygame, colour as col, dimensions as dim, buttons as but

screen = pygame.display.set_mode((dim.width, dim.height))
game_start = 0

def text(text, colour, x, y, size):
    font = pygame.font.Font('freesansbold.ttf', size)
    text = font.render(text, True, colour)
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)
    

def text_1(text, colour, colour_1, x, y, size, rotate):
    font = pygame.font.Font('freesansbold.ttf', size)
    text = font.render(text, True, colour, colour_1)
    textRect = text.get_rect()
    textRect.center = (x, y)
    text = pygame.transform.rotate(text, rotate)
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
    
    #Name Countries + Stats
    text_1('Madagascar', col.BLACK, None, 803, 631, 15, 60)
    text_1('South', col.BLACK, None, 670, 652, 15, 0)
    text_1('Africa', col.BLACK, None, 670, 667, 15, 0)
    text_1('Congo', col.BLACK, None, 662, 564, 15, 0)
    text_1('East', col.BLACK, None, 715, 517, 15, 0)
    text_1('Africa', col.BLACK, None, 740, 532, 15, 0)
    text_1('Africa', col.BLACK, None, 605, 480, 16, 0)
    text_1('North', col.BLACK, None, 547, 480, 16, 0)
    text_1('Egypt', col.BLACK, None, 665, 440, 15, 0)
    text_1('Middle East', col.BLACK, None, 773, 376, 15, 0)
    text_1('India', col.BLACK, None, 904, 389, 15, 0)
    text_1('Siam', col.BLACK, None, 1002, 424, 15, 0)
    text_1('China', col.BLACK, None, 979, 333, 15, 0)
    text_1('Mongolia', col.BLACK, None, 1015, 260, 15, 0)
    text_1('Japan', col.BLACK, None, 1145, 270, 15, 0)
    text_1('Afghanistan', col.BLACK, None, 843, 276, 15, 0)
    text_1('Ural', col.BLACK, None, 855, 181, 15, 0)
    text_1('Siberia', col.BLACK, None, 925, 121, 15, 0)
    text_1('Yakutsk', col.BLACK, None, 1025, 92, 15, 0)
    text_1('Irkutsk', col.BLACK, None, 1013, 185, 15, 0)
    text_1('Kamchatka', col.BLACK, None, 1125, 93, 15, 0)
    text_1('Ukraine', col.BLACK, None, 734, 188, 16, 0)
    text_1('Scandinavia', col.BLACK, None, 632, 112, 15, 45)
    text_1('Northern', col.BLACK, None, 617, 250, 15, 0)
    text_1('Europe', col.BLACK, None, 618, 263, 15, 0)
    text_1('Southern', col.BLACK, None, 620, 310, 15, 0)
    text_1('Europe', col.BLACK, None, 640, 324, 15, 0)
    text_1('Iceland', col.BLACK, None, 527, 150, 15, 0)
    text_1('Great Britian', col.BLACK, None, 493, 239, 15, 0)
    text_1('Western Europe', col.BLACK, None, 548, 292, 15, 55)
    text_1('Greenland', col.BLACK, None, 425, 76, 15, 0)
    text_1('Quebec', col.BLACK, None, 352, 194, 15, 0)
    text_1('Ontario', col.BLACK, None, 262, 195, 15, 0)
    text_1('Alberta', col.BLACK, None, 184, 180, 15, 0)
    text_1('Northwest Territoy', col.BLACK, None, 200, 117, 15, 0)
    text_1('Alaska', col.BLACK, None, 80, 120, 15, 0)
    text_1('Western', col.BLACK, None, 190, 245, 15, 0)
    text_1('United States', col.BLACK, None, 194, 262, 15, 0)
    text_1('Eastern', col.BLACK, None, 270, 286, 15, 0)
    text_1('United States', col.BLACK, None, 270, 298, 15, 0)
    text_1('Argentina', col.BLACK, None, 325, 605, 15, 0)
    text_1('Peru', col.BLACK, None, 313, 533, 15, 0)
    text_1('Brazil', col.BLACK, None, 371, 492, 16, 0)
    text_1('Venezuela', col.BLACK, None, 286, 426, 15, 0)
    text_1('Eastern', col.BLACK, None, 1159, 625, 15, 0)
    text_1('Australia', col.BLACK, None, 1158, 637, 15, 0)
    text_1('Western', col.BLACK, None, 1063, 655, 15, 0)
    text_1('Australia', col.BLACK, None, 1088, 669, 15, 0)
    text_1('New', col.BLACK, None, 1130, 512, 15, 0)
    text_1('Guinea', col.BLACK, None, 1138, 525, 15, 0)
    text_1('Ind', col.BLACK, None, 998, 548, 16, 15)
    text_1('one', col.BLACK, None, 1024, 548, 16, 0)
    text_1('sia', col.BLACK, None, 1049, 548, 16, -15)
    text_1('Central', col.BLACK, None, 194, 314, 15, -72)
    text_1('America', col.BLACK, None, 220, 368, 15, -18)


def start_screen():
    rect(col.DARK_BROWN, dim.map_center - 300, 250, 600, 250)
    rect(col.RED, dim.map_center - 280, 270, 560, 210)
    rect(col.DARK_BROWN, dim.map_center - 275, 275, 550, 200)
    text('Fishing For Bass', col.BLACK, dim.map_center, dim.height / 2, 50)

    
def start_menu():
    rect(col.BLACK, dim.map_center + 175, 435, 80, 30)
    rect(col.RED, dim.map_center + 178, 438, 74, 24)
    text('Click to Start', col.BLACK, dim.map_center + 215, 450, 10)


def end_menu():
    rect(col.BLACK, 18, 698, 84, 34)
    rect(col.RED, 20, 700, 80, 30)
    text('End Turn', col.BLACK, 60, 715, 15)


def start_game(x, y, left):        
    global game_start
    if game_start > 0:
        end_menu()
    elif but.start_button(x, y, left) > 0:
        game_start = 1    
    else:
        start_screen()
        start_menu()


def turn_stats(x, y, left, turn):
    text('{}'.format(turn), col.BLACK, dim.shop_column_2 + 25, 245, 30)
    but.end_button(x, y, left)