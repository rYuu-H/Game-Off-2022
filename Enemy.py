import math
import pygame
import random

class minion:
    def __init__(self,health=10,speed=random.randint(75,150),lv=1,size = 30):
        self.x= 0
        self.y= 0
        self.size = size
        self.rect = pygame.Rect(self.x,self.y,self.size,self.size)
        self.health = health
        self.speed = random.randint(75,200)
        self.lv=lv
        self.color = (0,0,255)

    def draw(self, win):
        pygame.draw.rect(win, self.color,self.rect)
    
    def update(self,player,FPS):
        speed = self.speed/FPS
        vector_x, vector_y = player.x - self.x, player.y - self.y
        distance = math.hypot(vector_x, vector_y)
        if distance != 0:
            move_vec = (speed * vector_x / distance, speed * vector_y / distance)
            self.x += move_vec[0]
            self.y += move_vec[1]

        self.rect = pygame.Rect(self.x ,self.y ,self.size ,self.size)