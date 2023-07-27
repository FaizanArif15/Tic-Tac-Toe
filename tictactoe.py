import pygame
from pygame.locals import *
from time import *

# initialize pygame
pygame.init()

# screen property variables
screen_width = 400
screen_height = 400

# game variables
size_of_stroke = 2 # thickness of grid line
array_2d = []
check_mark = 1
winner = False
thickness = 3


# color variables
red_color = (255,0,0)
green_color = (0,255,0)
blue_color = (0,0,255)
# background_color = (168, 88, 98)
background_color = (0, 0, 0)
white_color = (255,255,255)

# set screen
screen = pygame.display.set_mode((screen_width,screen_height))

# set caption
pygame.display.set_caption("Tic Tac Toe")

# set background colour
screen.fill(background_color)

# update pygame
pygame.display.update()

def make_2d_array():
    
    global array_2d
    
    array_2d = []
    for i in range(3):
        row = [0]*3
        array_2d.append(row)

# make grid lines
def make_grid():
    for i in range(1,3):
        pygame.draw.line(screen,white_color,(screen_width//3*i,0),(screen_width//3*i,screen_height),size_of_stroke)
        pygame.draw.line(screen,white_color,(0,screen_height//3*i),(screen_width,screen_height//3*i),size_of_stroke)
        
# display mark on grid
def display_mark(x,y):
    global thickness,red_color
    if check_mark == 1:
        pygame.draw.circle(screen,blue_color,((x*(screen_width//3))+((screen_width//3)//2),((y*(screen_width//3))+((screen_width//3)//2))),screen_width//10,thickness)
    else:
        pygame.draw.line(screen,red_color,((x*(screen_width//3))+((screen_width//3)//4),(y*(screen_height//3))+((screen_height//3)//4)),((x*(screen_width//3))+((screen_width//3)-((screen_width//3)//4)),(y*(screen_height//3))+((screen_height//3)-((screen_height//3)//4))),thickness)
        pygame.draw.line(screen,red_color,((x*(screen_width//3))+((screen_width//3)-((screen_width//3)//4)),(y*(screen_height//3))+((screen_width//3)//4)),((x*(screen_width//3))+((screen_height//3)//4),(y*(screen_height//3))+((screen_width//3)-(screen_height//3)//4)),thickness)

# check for who is winner
def checking_for_winner():
    
    global winner,thickness
    
    # check for first row
    x = 0
    y = 2
    if array_2d[0][0] == 1 and array_2d[0][1] == 1 and array_2d[0][2] == 1:
        winner = "Player 1 Win"
        pygame.draw.line(screen,green_color,((x*(screen_width//3))+((screen_width//3)//4),(x*(screen_height//3))+((screen_height//3)//4)*2),((y*(screen_width//3))+((screen_width//3)-((screen_width//3)//4)),(x*(screen_height//3))+((screen_height//3)//4)*2),thickness)
        return
    elif array_2d[0][0] == 2 and array_2d[0][1] == 2 and array_2d[0][2] == 2:
        winner = "Player 2 Win"
        pygame.draw.line(screen,green_color,((x*(screen_width//3))+((screen_width//3)//4),(x*(screen_height//3))+((screen_height//3)//4)*2),((y*(screen_width//3))+((screen_width//3)-((screen_width//3)//4)),(x*(screen_height//3))+((screen_height//3)//4)*2),thickness)
        return
    
    # check for second row
    x = 0
    y = 2
    if array_2d[1][0] == 1 and array_2d[1][1] == 1 and array_2d[1][2] == 1:
        winner = "Player 1 Win"
        pygame.draw.line(screen,green_color,((x*(screen_width//3))+((screen_width//3)//4),((x+1)*(screen_height//3))+((screen_height//3)//4)*2),((y*(screen_width//3))+((screen_width//3)-((screen_width//3)//4)),((x+1)*(screen_height//3))+((screen_height//3)//4)*2),thickness)
        return
    elif array_2d[1][0] == 2 and array_2d[1][1] == 2 and array_2d[1][2] == 2:
        winner = "Player 2 Win"
        pygame.draw.line(screen,green_color,((x*(screen_width//3))+((screen_width//3)//4),((x+1)*(screen_height//3))+((screen_height//3)//4)*2),((y*(screen_width//3))+((screen_width//3)-((screen_width//3)//4)),((x+1)*(screen_height//3))+((screen_height//3)//4)*2),thickness)
        return
    
    # check for third row
    x = 0
    y = 2
    if array_2d[2][0] == 1 and array_2d[2][1] == 1 and array_2d[2][2] == 1:
        winner = "Player 1 Win"
        pygame.draw.line(screen,green_color,((x*(screen_width//3))+((screen_width//3)//4),((x+2)*(screen_height//3))+((screen_height//3)//4)*2),((y*(screen_width//3))+((screen_width//3)-((screen_width//3)//4)),((x+2)*(screen_height//3))+((screen_height//3)//4)*2),thickness)
        return
    elif array_2d[2][0] == 2 and array_2d[2][1] == 2 and array_2d[2][2] == 2:
        winner = "Player 2 Win"
        pygame.draw.line(screen,green_color,((x*(screen_width//3))+((screen_width//3)//4),((x+2)*(screen_height//3))+((screen_height//3)//4)*2),((y*(screen_width//3))+((screen_width//3)-((screen_width//3)//4)),((x+2)*(screen_height//3))+((screen_height//3)//4)*2),thickness)
        return
    
    # check for first colum
    x = 0
    y = 2
    if array_2d[0][0] == 1 and array_2d[1][0] == 1 and array_2d[2][0] == 1:
        winner = "Player 1 Win"
        pygame.draw.line(screen,green_color,((x*(screen_width//3))+((screen_width//3)//2),((screen_height//3)//4)),((x*(screen_width//3))+(((screen_width//3)//2)),(y*(screen_height//3))+(screen_height//3)-((screen_height//3)//4)),thickness)
        return
    elif array_2d[0][0] == 2 and array_2d[1][0] == 2 and array_2d[2][0] == 2:
        winner = "Player 2 Win"
        pygame.draw.line(screen,green_color,((x*(screen_width//3))+((screen_width//3)//2),((screen_height//3)//4)),((x*(screen_width//3))+(((screen_width//3)//2)),(y*(screen_height//3))+(screen_width//3)-((screen_height//3)//4)),thickness)
        return
    
    # check for second colum
    x = 1
    y = 2
    if array_2d[0][1] == 1 and array_2d[1][1] == 1 and array_2d[2][1] == 1:
        winner = "Player 1 Win"
        pygame.draw.line(screen,green_color,((x*(screen_width//3))+((screen_width//3)//2),((screen_height//3)//4)),((x*(screen_width//3))+(((screen_width//3)//2)),(y*(screen_height//3))+(screen_height//3)-((screen_height//3)//4)),thickness)
        return
    elif array_2d[0][1] == 2 and array_2d[1][1] == 2 and array_2d[2][1] == 2:
        winner = "Player 2 Win"
        pygame.draw.line(screen,green_color,((x*(screen_width//3))+((screen_width//3)//2),((screen_height//3)//4)),((x*(screen_width//3))+(((screen_width//3)//2)),(y*(screen_height//3))+(screen_height//3)-((screen_height//3)//4)),thickness)
        return
        
    # check for third colum
    x = 2
    y = 2
    if array_2d[0][2] == 1 and array_2d[1][2] == 1 and array_2d[2][2] == 1:
        winner = "Player 1 Win"
        pygame.draw.line(screen,green_color,((x*(screen_width//3))+((screen_width//3)//2),((screen_height//3)//4)),((x*(screen_width//3))+(((screen_width//3)//2)),(y*(screen_height//3))+(screen_height//3)-((screen_height//3)//4)),thickness)
        return
    elif array_2d[0][2] == 2 and array_2d[1][2] == 2 and array_2d[2][2] == 2:
        winner = "Player 2 Win"
        pygame.draw.line(screen,green_color,((x*(screen_width//3))+((screen_width//3)//2),((screen_height//3)//4)),((x*(screen_width//3))+(((screen_width//3)//2)),(y*(screen_height//3))+(screen_height//3)-((screen_height//3)//4)),thickness)
        return
        
    # check for diagonal upper left to lower right
    x = 0
    y = 2
    if array_2d[0][0] == 1 and array_2d[1][1] == 1 and array_2d[2][2] == 1:
        winner = "Player 1 Win"
        pygame.draw.line(screen,green_color,((x*(screen_width//3))+((screen_width//3)//4),(x*(screen_height//3))+((screen_height//3)//4)),((y*(screen_width//3))+((screen_width//3)-((screen_width//3)//4)),(y*(screen_height//3))+((screen_height//3)-((screen_height//3)//4))),thickness)
        return
    elif array_2d[0][0] == 2 and array_2d[1][1] == 2 and array_2d[2][2] == 2:
        winner = "Player 2 Win"
        pygame.draw.line(screen,green_color,((x*(screen_width//3))+((screen_width//3)//4),(x*(screen_height//3))+((screen_height//3)//4)),((y*(screen_width//3))+((screen_width//3)-((screen_width//3)//4)),(y*(screen_height//3))+((screen_height//3)-((screen_height//3)//4))),thickness)
        return
    
    # check for diagonal upper right to lower left
    x = 2
    y = 0
    if array_2d[0][2] == 1 and array_2d[1][1] == 1 and array_2d[2][0] == 1:
        winner = "Player 1 Win"
        pygame.draw.line(screen,green_color,((x*(screen_width//3))+((screen_width//3)-((screen_width//3)//4)),(y*(screen_height//3))+((screen_width//3)//4)),((y*(screen_width//3))+((screen_height//3)//4),(x*(screen_height//3))+((screen_width//3)-(screen_height//3)//4)),thickness)
        return
    elif array_2d[0][2] == 2 and array_2d[1][1] == 2 and array_2d[2][0] == 2:
        winner = "Player 2 Win"
        pygame.draw.line(screen,green_color,((x*(screen_width//3))+((screen_width//3)-((screen_width//3)//4)),(y*(screen_height//3))+((screen_width//3)//4)),((y*(screen_width//3))+((screen_height//3)//4),(x*(screen_height//3))+((screen_width//3)-(screen_height//3)//4)),thickness)
        return
    
    # check for draw match
    if not any(0 in item for item in array_2d):
        winner = "Draw Match"
        

def display_text(font="calibri", size=48,position=(screen_width//2,screen_height//2-50), color = (0,0,0),background_color = (0,0,255)):
    
    global winner
    
    calibri = pygame.font.SysFont(font, size)
    text = calibri.render(winner, True, color,background_color)
    text_rect = text.get_rect()
    text_rect.center = position
    screen.blit(text, text_rect)

if __name__ == "__main__":
    
    run = True
    
    make_2d_array()
    make_grid()
    while run and not winner:
        
        # control events
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                run = False
            elif event.type == MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                x = mouse_position[0]//(screen_width//3) # x is equal to width,column
                y = mouse_position[1]//(screen_height//3) # y is equal to height,row
                if array_2d[y][x] == 0:
                    
                    display_mark(x,y)
                    
                    if check_mark == 1:
                        array_2d[y][x] = 1
                    elif check_mark == -1:
                        array_2d[y][x] = 2
                    check_mark *= -1
                    
                    checking_for_winner()
                    pygame.display.update()
                    if winner:
                        sleep(0.5)
                        display_text(color=(144,23,69),background_color=(255, 255, 255))
        
        pygame.display.update()
        
        if winner:
            
            sleep(0.5)
            if "Player" in winner:
                winner = "Play Again?"
            else:
                winner = "Try Again"
            display_text('vista',48,(screen_width//2,screen_height//2+50),(255,255,255),(240,19,225))
            winner = False
            pygame.display.update()

            loop = True
            while loop:
                
                for event in pygame.event.get():
                    if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                        run = False
                        loop = False
                    elif event.type == MOUSEBUTTONDOWN:
                        screen.fill(background_color)
                        make_2d_array()
                        make_grid()
                        pygame.display.update()
                        loop = False
    
    