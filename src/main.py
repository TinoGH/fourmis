
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((1000, 1000))

from map.Map import Map
from gui.Board import Board
import map.coordinates as coords


map = Map(6)
map.create_unit((0, 0, 0), "ant")
map.create_unit((-1, 1, 0), "ant")
board = Board(900, map)
map_pos = (50, 100)

play = True
cell_coordinates = (None, None, None)
while play:

    screen.fill([255, 255, 255])
    board.update_surface()

    event = pygame.event.wait()
    if event.type == QUIT:
        play = False
    elif event.type == MOUSEMOTION:
        mouse_pos = pygame.mouse.get_pos()
        cell_coordinates = coords.from_cartesian(board.pixels_to_cartesian(mouse_pos, map_pos))
    elif event.type == MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        cell_coordinates = coords.from_cartesian(board.pixels_to_cartesian(mouse_pos, map_pos))
        if map.get_selection() != (None, None, None):
            if cell_coordinates in coords.neighbours(map.get_selection()):
                direction = coords.neighbours(map.get_selection()).index(cell_coordinates)
                if map.move_selection(direction):
                    map.deselect()
        else:
            if map.get_cell(cell_coordinates) is not False:
                if map.get_cell(cell_coordinates).get_name() != "empty":
                    map.select(cell_coordinates)
    else:
        pass

    board.highlight(cell_coordinates)
    screen.blit(board.get_surface(), map_pos)
    pygame.display.flip()
