import pygame, sys
from Player import Player
from pygame.locals import *






def main():

    pygame.init()
    # # load and set the logo
    # logo = pygame.image.load("logo32x32.png")
    # pygame.display.set_icon(logo)
    # pygame.display.set_caption("minimal program")
    WIDTH  = 480
    HEIGHT = 480
    win = pygame.display.set_mode((WIDTH,HEIGHT))
    FPS = 240
    clock = pygame.time.Clock()
    
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