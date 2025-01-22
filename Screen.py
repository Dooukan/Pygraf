import pygame
import sys
import math
from settings import *



class Scr:
    def __init__(self):

        self.width = halfWIDTH
        self.height = halfHEIGHT
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        #wraping X and Y defult value I did use halfwith for centering but if you change wrap it gona change senter point without any interaption. 
        #If you add or change some code you can easly make this code workable in little screen on your code but I start project for this basic version so...
        self.WrapX = 0
        self.WrapY = 0
        self.x = X
        self.y = Y
        self.button0 = False
        self.button1 = False
        self.function_input = "math.sin(x)"  # your function here accept only math libary and basic calculation x+x x*x vs

    def draw(self):#this draw just draw condination lines you could add draw function here for showing mouse cordination
        self.screen.fill(BACKGROUND)
        pygame.draw.line(self.screen, LINES, (self.width-self.x + self.WrapX, 0), (self.width-self.x + self.WrapX, HEIGHT))
        pygame.draw.line(self.screen, LINES, (0, self.height-self.y + self.WrapY), (WIDTH, self.height-self.y + self.WrapY))
        self.draw_function()
        pygame.display.flip()

    def draw_function(self):
        

        for _ in range(-WIDTH,WIDTH):
            x=  _+ self.width-self.x#notaion 1
            try:
                y = eval(self.function_input.replace("x", str(x / 100))) * 100#HERE
                """evalotion if you wanna change density of the points change last muiltication lover 
                        and mult notaion 1 and 2's as much as you loverd"""

                if 0<self.height-self.y-y < HEIGHT:#notation 2 midle one
                    pygame.draw.rect(self.screen, grafLINES, (self.width-self.x - x, self.height-self.y - y, 1,1),1)
            except:
                pass

    def isOn(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pygame.mouse.get_pressed(3)[0]:
                self.button1 = True

    def update(self):
        self.isOn()
        self.draw()

    def run(self):
        while True:
            x, y = pygame.mouse.get_pos()
            self.update()
            if self.button1:
                x0, y0 = pygame.mouse.get_pos()
                #I hate code in here I need to change all this pre defined here but it is works
                if 0 <= self.width-self.x + self.WrapX <= WIDTH and 0 <= self.height-self.y + self.WrapY <= HEIGHT:
                    self.button1 = False
                    self.x -= -x + x0
                    self.y -= -y + y0
                if self.width-self.x + self.WrapX < 0:
                    self.WrapX += WIDTH
                elif self.width-self.x + self.WrapX > WIDTH:
                    self.WrapX -= WIDTH
                if self.height-self.y + self.WrapY < 0:
                    self.WrapY += HEIGHT
                elif self.height-self.y + self.WrapY > HEIGHT:
                    self.WrapY -= HEIGHT
            

main = Scr()
main.run()

