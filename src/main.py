
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((1000, 1000))

from map.Map import Map
from map.Coordinates import Coordinates
from gui.Board import Board


map = Map(1)
board = Board(1000, map)

play = True
cell_coordinates = Coordinates((0, 0, 0))
while play:
    screen.fill([255, 255, 255])

    event = pygame.event.wait()
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

    elif event.type == MOUSEMOTION:
        mouse_pos = pygame.mouse.get_pos()
        if board.cartesian_to_coordinates(mouse_pos).get_values() != cell_coordinates.get_values():
            cell_coordinates = board.cartesian_to_coordinates(mouse_pos)
            print(cell_coordinates)
    else:
        pass

    screen.blit(board.highlight(cell_coordinates), (0, 0))
    pygame.display.flip()
