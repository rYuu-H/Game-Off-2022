
import pygame, sys , math
from Player import Player
from pygame.locals import *

def bounce(bullet,win):
    out = True
    width = win.get_width()
    height = win.get_height()
    move_vec = list(bullet[2])
    while out == True :
        if bullet[0] <= 0:
            bullet[0] *= -1
            move_vec[0] *= -1
            bullet[2] = move_vec
        if bullet[0] >= width:
            bullet[0] -= (bullet[0] -width)*2
            move_vec[0] *= -1
            bullet[2] = move_vec
        if bullet[1] <= 0:
            bullet[1] *= -1
            move_vec[1] *= -1
            bullet[2] = move_vec
        if bullet[1] >= height:
            bullet[1] -= (bullet[1] -height)*2
            move_vec[1] *= -1
            bullet[2] = move_vec




        out = False


def spawn_bullet(list_of_bullets, x, y , speed=50):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    vector_x, vector_y = mouse_x - x, mouse_y - y
    distance = math.hypot(vector_x, vector_y)
    if distance == 0:
        return
    move_vec = (speed * vector_x / distance, speed * vector_y / distance)
    list_of_bullets.append([x, y, move_vec])



def main():
    
    pygame.init()
    # # load and set the logo
    # logo = pygame.image.load("logo32x32.png")
    # pygame.display.set_icon(logo)
    # pygame.display.set_caption("minimal program")
    WIDTH  = 480
    HEIGHT = 480
    win = pygame.display.set_mode((WIDTH,HEIGHT))
    FPS = 60
    clock = pygame.time.Clock()
    bullets = []
    player = Player(WIDTH/2, HEIGHT/2,WIDTH,HEIGHT)
    running = True
     
    # main loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                player.shooting = True

            if event.type == pygame.MOUSEBUTTONUP:
                player.shooting = False

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.a = True
                if event.key == pygame.K_d:
                    player.d = True
                if event.key == pygame.K_w:
                    player.w = True
                if event.key == pygame.K_s:
                    player.s = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player.a = False
                if event.key == pygame.K_d:
                    player.d = False
                if event.key == pygame.K_w:
                    player.w = False
                if event.key == pygame.K_s:
                    player.s = False
        x, y = pygame.mouse.get_pos()     
        win.fill((100,100,100))


        if player.shooting:
            if player.frameUntillNext <= 0:
            # pygame.draw.line(win,(255,0,0),((player.x+player.size/2),(player.y+player.size/2)),(x,y))
                spawn_bullet(bullets,player.x+player.size/2,player.y+player.size/2,300/FPS)  
                player.frameUntillNext += FPS/ player.aps


        for bullet in bullets:
            bullet[0] += bullet[2][0]
            bullet[1] += bullet[2][1]
            bounce(bullet,win)
            if not (0-50 <= bullet[0] < win.get_width()+50 and 0-50 < bullet[1] < win.get_height())+50:
                del bullets[bullets.index(bullet)]
                continue
            pygame.draw.circle(win,(0,255,255),(bullet[0],bullet[1]),10)
        pygame.draw.line(win,(255,0,0),((player.x+player.size/2),(player.y+player.size/2)),(x,y))
        player.draw(win)
        
        player.update(FPS)
        pygame.display.flip()
        # print(player.shooting)
        # print(pygame.mouse.get_pos())
        print(player.x,player.y)
        clock.tick(FPS)
                
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()