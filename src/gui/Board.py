
import pygame
from map.Map import Map
from map.Hex import Hex
from math import floor


class Board:
    """

    """

    images_path = "./media/pixel_art/"
    images = dict()
    for hex_type in Hex.hex_list:
        images[hex_type] = pygame.image.load(images_path + hex_type + ".png").convert_alpha()

    def __init__(self, size: int):
        """

        :param size:
        """
        self._surface = pygame.Surface((size, size))
        self._size = size

    def get_surface(self, map: 'Map'):
        """

        :param map:
        :return:
        """
        self._surface.fill([255, 255, 255])
        hex_size = floor(self._size / (2 * (map.get_radius() + 1)))
        for cell in map.get_grid().values():
            x, y = cell.get_coordinates().to_cartesian()
            x = x * hex_size - hex_size / 2 + self._size / 2
            y = y * hex_size - hex_size / 2 + self._size / 2
            hex_surface = pygame.transform.rotate(
                pygame.transform.scale(Board.images[cell.get_name()], (hex_size, hex_size)),
                cell.get_orientation() * 60)
            w, h = hex_surface.get_size()
            x = x - (w - hex_size) / 2
            y = y - (h - hex_size) / 2
            self._surface.blit(hex_surface, (x, y))
        return self._surface
