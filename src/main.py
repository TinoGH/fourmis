
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((1000, 1000))

from map.Map import Map
from gui.Board import Board


map = Map(8)
board = Board(1000)

play = True
while play:
    for event in pygame.event.get():
        if event.type == QUIT:
            play = False
        elif event.type == KEYDOWN:
            useful_key = True
            direction = 0
            if event.key == K_d:
                direction = 0
            elif event.key == K_e:
                direction = 1
            elif event.key == K_w:
                direction = 2
            elif event.key == K_a:
                direction = 3
            elif event.key == K_z:
                direction = 4
            elif event.key == K_x:
                direction = 5
            elif event.key == K_ESCAPE:
                play = False
                useful_key = False
            else:
                useful_key = False

            if useful_key:
                map.move_selection(direction)
        else:
            pass

    screen.fill([255, 255, 255])
    screen.blit(board.get_surface(map), (0, 0))
    pygame.display.flip()
