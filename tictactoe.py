import pygame
from pygame.locals import *
from time import *
import asyncio


class Game:
    
    def __init__(self,width,height,background_colour) -> None:
        
        # screen property variables
        self.screen_width = width
        self.screen_height = height

        # game variables
        self.size_of_stroke = 2 # thickness of grid line
        self.array_2d = []
        self.check_mark = 1
        self.winner = False
        self.thickness = 3


        # color variables
        self.red_color = (255,0,0)
        self.green_color = (0,255,0)
        self.blue_color = (0,0,255)
        self.background_color = background_colour
        self.white_color = (255,255,255)


    def make_2d_array(self):
                
        # self.array_2d = []
        for i in range(3):
            row = [0]*3
            self.array_2d.append(row)

    # make grid lines
    def make_grid(self):
        for i in range(1,3):
            pygame.draw.line(screen,self.white_color,(self.screen_width//3*i,0),(self.screen_width//3*i,self.screen_height),self.size_of_stroke)
            pygame.draw.line(screen,self.white_color,(0,self.screen_height//3*i),(self.screen_width,self.screen_height//3*i),self.size_of_stroke)
            
    # display mark on grid
    def display_mark(self,x,y):
        if self.check_mark == 1:
            pygame.draw.circle(screen,self.blue_color,((x*(self.screen_width//3))+((self.screen_width//3)//2),((y*(self.screen_width//3))+((self.screen_width//3)//2))),self.screen_width//10,self.thickness)
        else:
            pygame.draw.line(screen,self.red_color,((x*(self.screen_width//3))+((self.screen_width//3)//4),(y*(self.screen_height//3))+((self.screen_height//3)//4)),((x*(self.screen_width//3))+((self.screen_width//3)-((self.screen_width//3)//4)),(y*(self.screen_height//3))+((self.screen_height//3)-((self.screen_height//3)//4))),self.thickness)
            pygame.draw.line(screen,self.red_color,((x*(self.screen_width//3))+((self.screen_width//3)-((self.screen_width//3)//4)),(y*(self.screen_height//3))+((self.screen_width//3)//4)),((x*(self.screen_width//3))+((self.screen_height//3)//4),(y*(self.screen_height//3))+((self.screen_width//3)-(self.screen_height//3)//4)),self.thickness)

    # check for who is self.winner
    def checking_for_winner(self):
        
        # check for first row
        x = 0
        y = 2
        if self.array_2d[0][0] == 1 and self.array_2d[0][1] == 1 and self.array_2d[0][2] == 1:
            self.winner = "Player 1 Win"
            pygame.draw.line(screen,self.green_color,((x*(self.screen_width//3))+((self.screen_width//3)//4),(x*(self.screen_height//3))+((self.screen_height//3)//4)*2),((y*(self.screen_width//3))+((self.screen_width//3)-((self.screen_width//3)//4)),(x*(self.screen_height//3))+((self.screen_height//3)//4)*2),self.thickness)
            return
        elif self.array_2d[0][0] == 2 and self.array_2d[0][1] == 2 and self.array_2d[0][2] == 2:
            self.winner = "Player 2 Win"
            pygame.draw.line(screen,self.green_color,((x*(self.screen_width//3))+((self.screen_width//3)//4),(x*(self.screen_height//3))+((self.screen_height//3)//4)*2),((y*(self.screen_width//3))+((self.screen_width//3)-((self.screen_width//3)//4)),(x*(self.screen_height//3))+((self.screen_height//3)//4)*2),self.thickness)
            return
        
        # check for second row
        x = 0
        y = 2
        if self.array_2d[1][0] == 1 and self.array_2d[1][1] == 1 and self.array_2d[1][2] == 1:
            self.winner = "Player 1 Win"
            pygame.draw.line(screen,self.green_color,((x*(self.screen_width//3))+((self.screen_width//3)//4),((x+1)*(self.screen_height//3))+((self.screen_height//3)//4)*2),((y*(self.screen_width//3))+((self.screen_width//3)-((self.screen_width//3)//4)),((x+1)*(self.screen_height//3))+((self.screen_height//3)//4)*2),self.thickness)
            return
        elif self.array_2d[1][0] == 2 and self.array_2d[1][1] == 2 and self.array_2d[1][2] == 2:
            self.winner = "Player 2 Win"
            pygame.draw.line(screen,self.green_color,((x*(self.screen_width//3))+((self.screen_width//3)//4),((x+1)*(self.screen_height//3))+((self.screen_height//3)//4)*2),((y*(self.screen_width//3))+((self.screen_width//3)-((self.screen_width//3)//4)),((x+1)*(self.screen_height//3))+((self.screen_height//3)//4)*2),self.thickness)
            return
        
        # check for third row
        x = 0
        y = 2
        if self.array_2d[2][0] == 1 and self.array_2d[2][1] == 1 and self.array_2d[2][2] == 1:
            self.winner = "Player 1 Win"
            pygame.draw.line(screen,self.green_color,((x*(self.screen_width//3))+((self.screen_width//3)//4),((x+2)*(self.screen_height//3))+((self.screen_height//3)//4)*2),((y*(self.screen_width//3))+((self.screen_width//3)-((self.screen_width//3)//4)),((x+2)*(self.screen_height//3))+((self.screen_height//3)//4)*2),self.thickness)
            return
        elif self.array_2d[2][0] == 2 and self.array_2d[2][1] == 2 and self.array_2d[2][2] == 2:
            self.winner = "Player 2 Win"
            pygame.draw.line(screen,self.green_color,((x*(self.screen_width//3))+((self.screen_width//3)//4),((x+2)*(self.screen_height//3))+((self.screen_height//3)//4)*2),((y*(self.screen_width//3))+((self.screen_width//3)-((self.screen_width//3)//4)),((x+2)*(self.screen_height//3))+((self.screen_height//3)//4)*2),self.thickness)
            return
        
        # check for first colum
        x = 0
        y = 2
        if self.array_2d[0][0] == 1 and self.array_2d[1][0] == 1 and self.array_2d[2][0] == 1:
            self.winner = "Player 1 Win"
            pygame.draw.line(screen,self.green_color,((x*(self.screen_width//3))+((self.screen_width//3)//2),((self.screen_height//3)//4)),((x*(self.screen_width//3))+(((self.screen_width//3)//2)),(y*(self.screen_height//3))+(self.screen_height//3)-((self.screen_height//3)//4)),self.thickness)
            return
        elif self.array_2d[0][0] == 2 and self.array_2d[1][0] == 2 and self.array_2d[2][0] == 2:
            self.winner = "Player 2 Win"
            pygame.draw.line(screen,self.green_color,((x*(self.screen_width//3))+((self.screen_width//3)//2),((self.screen_height//3)//4)),((x*(self.screen_width//3))+(((self.screen_width//3)//2)),(y*(self.screen_height//3))+(self.screen_width//3)-((self.screen_height//3)//4)),self.thickness)
            return
        
        # check for second colum
        x = 1
        y = 2
        if self.array_2d[0][1] == 1 and self.array_2d[1][1] == 1 and self.array_2d[2][1] == 1:
            self.winner = "Player 1 Win"
            pygame.draw.line(screen,self.green_color,((x*(self.screen_width//3))+((self.screen_width//3)//2),((self.screen_height//3)//4)),((x*(self.screen_width//3))+(((self.screen_width//3)//2)),(y*(self.screen_height//3))+(self.screen_height//3)-((self.screen_height//3)//4)),self.thickness)
            return
        elif self.array_2d[0][1] == 2 and self.array_2d[1][1] == 2 and self.array_2d[2][1] == 2:
            self.winner = "Player 2 Win"
            pygame.draw.line(screen,self.green_color,((x*(self.screen_width//3))+((self.screen_width//3)//2),((self.screen_height//3)//4)),((x*(self.screen_width//3))+(((self.screen_width//3)//2)),(y*(self.screen_height//3))+(self.screen_height//3)-((self.screen_height//3)//4)),self.thickness)
            return
            
        # check for third colum
        x = 2
        y = 2
        if self.array_2d[0][2] == 1 and self.array_2d[1][2] == 1 and self.array_2d[2][2] == 1:
            self.winner = "Player 1 Win"
            pygame.draw.line(screen,self.green_color,((x*(self.screen_width//3))+((self.screen_width//3)//2),((self.screen_height//3)//4)),((x*(self.screen_width//3))+(((self.screen_width//3)//2)),(y*(self.screen_height//3))+(self.screen_height//3)-((self.screen_height//3)//4)),self.thickness)
            return
        elif self.array_2d[0][2] == 2 and self.array_2d[1][2] == 2 and self.array_2d[2][2] == 2:
            self.winner = "Player 2 Win"
            pygame.draw.line(screen,self.green_color,((x*(self.screen_width//3))+((self.screen_width//3)//2),((self.screen_height//3)//4)),((x*(self.screen_width//3))+(((self.screen_width//3)//2)),(y*(self.screen_height//3))+(self.screen_height//3)-((self.screen_height//3)//4)),self.thickness)
            return
            
        # check for diagonal upper left to lower right
        x = 0
        y = 2
        if self.array_2d[0][0] == 1 and self.array_2d[1][1] == 1 and self.array_2d[2][2] == 1:
            self.winner = "Player 1 Win"
            pygame.draw.line(screen,self.green_color,((x*(self.screen_width//3))+((self.screen_width//3)//4),(x*(self.screen_height//3))+((self.screen_height//3)//4)),((y*(self.screen_width//3))+((self.screen_width//3)-((self.screen_width//3)//4)),(y*(self.screen_height//3))+((self.screen_height//3)-((self.screen_height//3)//4))),self.thickness)
            return
        elif self.array_2d[0][0] == 2 and self.array_2d[1][1] == 2 and self.array_2d[2][2] == 2:
            self.winner = "Player 2 Win"
            pygame.draw.line(screen,self.green_color,((x*(self.screen_width//3))+((self.screen_width//3)//4),(x*(self.screen_height//3))+((self.screen_height//3)//4)),((y*(self.screen_width//3))+((self.screen_width//3)-((self.screen_width//3)//4)),(y*(self.screen_height//3))+((self.screen_height//3)-((self.screen_height//3)//4))),self.thickness)
            return
        
        # check for diagonal upper right to lower left
        x = 2
        y = 0
        if self.array_2d[0][2] == 1 and self.array_2d[1][1] == 1 and self.array_2d[2][0] == 1:
            self.winner = "Player 1 Win"
            pygame.draw.line(screen,self.green_color,((x*(self.screen_width//3))+((self.screen_width//3)-((self.screen_width//3)//4)),(y*(self.screen_height//3))+((self.screen_width//3)//4)),((y*(self.screen_width//3))+((self.screen_height//3)//4),(x*(self.screen_height//3))+((self.screen_width//3)-(self.screen_height//3)//4)),self.thickness)
            return
        elif self.array_2d[0][2] == 2 and self.array_2d[1][1] == 2 and self.array_2d[2][0] == 2:
            self.winner = "Player 2 Win"
            pygame.draw.line(screen,self.green_color,((x*(self.screen_width//3))+((self.screen_width//3)-((self.screen_width//3)//4)),(y*(self.screen_height//3))+((self.screen_width//3)//4)),((y*(self.screen_width//3))+((self.screen_height//3)//4),(x*(self.screen_height//3))+((self.screen_width//3)-(self.screen_height//3)//4)),self.thickness)
            return
        
        # check for draw match
        if not any(0 in item for item in self.array_2d):
            self.winner = "Draw Match"
            

    def display_text(self,font="calibri", size=48,position=0, color = (0,0,0),background_color = (0,0,255)):
        if position == 0:
            position = (self.screen_width//2,self.screen_height//2-50)
        calibri = pygame.font.SysFont(font, size)
        text = calibri.render(self.winner, True, color,self.background_color)
        text_rect = text.get_rect()
        text_rect.center = position
        screen.blit(text, text_rect)

    async def main(self): 

        run = True
        
        self.make_2d_array()
        self.make_grid()
        while run and not self.winner:
            
            # control events
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    run = False
                elif event.type == MOUSEBUTTONDOWN:
                    mouse_position = pygame.mouse.get_pos()
                    x = mouse_position[0]//(self.screen_width//3) # x is equal to width,column
                    y = mouse_position[1]//(self.screen_height//3) # y is equal to height,row
                    if self.array_2d[y][x] == 0:
                        
                        self.display_mark(x,y)
                        
                        if self.check_mark == 1:
                            self.array_2d[y][x] = 1
                        elif self.check_mark == -1:
                            self.array_2d[y][x] = 2
                        self.check_mark *= -1
                        
                        self.checking_for_winner()
                        pygame.display.update()
                        if self.winner:
                            sleep(0.5)
                            self.display_text(color=(144,23,69),background_color=(255, 255, 255))
            
            pygame.display.update()
            await asyncio.sleep(0)
            
            if self.winner:
                
                sleep(0.5)
                if "Player" in self.winner:
                    self.winner = "Play Again?"
                else:
                    self.winner = "Try Again"
                self.display_text('vista',48,(self.screen_width//2,self.screen_height//2+50),(255,255,255),(240,19,225))
                self.winner = False
                pygame.display.update()

                loop = True
                while loop:
                    
                    for event in pygame.event.get():
                        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                            run = False
                            loop = False
                        elif event.type == MOUSEBUTTONDOWN or event.type == KEYUP:
                            screen.fill(self.background_color)
                            self.array_2d.clear()
                            self.make_2d_array()
                            self.make_grid()
                            pygame.display.update()
                            await asyncio.sleep(0)
                            loop = False
        

if __name__ == "__main__":
    
    # initialize pygame
    pygame.init()
    
    # set screen
    screen_width = 400
    screen_height = 400
    screen = pygame.display.set_mode((screen_width,screen_height))

    # set caption
    pygame.display.set_caption("Tic Tac Toe")

    # set background colour
    background_color = (0,0,0)
    screen.fill(background_color)

    # update pygame
    pygame.display.update()
    
    # game = Game(screen_width,screen_height,background_color)
    asyncio.run(Game(screen_width,screen_height,background_color).main())
