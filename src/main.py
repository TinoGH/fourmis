
import pygame
from pygame.locals import *
from map.Coordinates import Coordinates
from map.Hex import Orientation
from map.Map import Map

screen = pygame.display.set_mode((800, 800))

map = Map(2)
print(map)

screen.fill([255, 255, 255])
screen.blit(map.get_surface(800), (0, 0))
pygame.display.flip()

while 1:
    continue
