import pygame
from pygame.locals import *
class Player:
    def __init__(self, x, y, WIDTH, HEIGHT):
        self.size = 30
        self.rect = pygame.Rect(x,y,self.size,self.size)
        self.WIDTH = WIDTH
        self.HEIGHT= HEIGHT
        self.x = int(x)
        self.y = int(y)
        self.color = (250,0,0)
        self.velX = 0
        self.celY = 0
        self.w =False
        self.s =False
        self.a =False
        self.d =False
        self.speed = 300
        self.shooting = False
        self.aps = 1
        self.frameUntillNext = 0

    def draw(self, win):
        pygame.draw.rect(win, self.color,self.rect)

    def update(self,FPS):
        self.velX = 0
        self.velY = 0
        if self.w and not self.s:
            self.velY = -self.speed 
        if self.s and not self.w:
            self.velY = self.speed 
        if self.a and not self.d:
            self.velX = -self.speed 
        if self.d and not self.a:
            self.velX = self.speed
        
        if not self.velX == 0 and self.velY == 0:
            self.velX == self.velX^2


        self.x += self.velX/FPS
        self.y += self.velY/FPS

        if self.x <= 0:
            self.x = 0 
        if self.x >= self.WIDTH - self.size:
            self.x = self.WIDTH - self.size
        if self.y <= 0:
            self.y = 0
        if self.y >= self.HEIGHT - self.size:
            self.y = self.HEIGHT - self.size
        
        if self.frameUntillNext > 0:
            self.frameUntillNext -= 1

        # if self.shooting :
        #     if self.frameUntillNext <= 0:
                # x, y = pygame.mouse.get_pos()
                # m = ((self.y + self.HEIGHT*0.5)-y)/((self.x + self.WIDTH*0.5)-x)
                # print(m)
                # pygame.draw.line()
                # self.frameUntillNext = self.aps * FPS


        self.rect = pygame.Rect(self.x ,self.y ,self.size ,self.size)