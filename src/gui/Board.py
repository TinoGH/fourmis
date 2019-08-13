
import pygame
from map.Map import Map
from map.Hex import Hex
from map.Coordinates import Coordinates
from math import floor, sqrt


class Board:
    """

    """

    images_path = "./media/pixel_art/"
    images = dict()
    for hex_type in Hex.hex_list:
        images[hex_type] = pygame.image.load(images_path + hex_type + ".png").convert_alpha()

    def __init__(self, size: int, map: 'Map'):
        """

        :param size:
        :param map:
        """
        self._surface = pygame.Surface((size, size))
        self._size = size
        self._map = map
        self._hex_size = floor(self._size / (2 * self._map.get_radius() + 1))

    def get_surface(self):
        """

        :param map:
        :return:
        """
        self._surface.fill([255, 255, 255])
        hex_size = self._hex_size
        for cell in self._map.get_grid().values():
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

    def cartesian_to_coordinates(self, coords: (int, int)):
        """

        :param coords:
        :return:
        """
        x, y = coords
        x, y = (x - self._size / 2) / self._hex_size , (y - self._size / 2) / self._hex_size
        X = round((2 / sqrt(3)) * x - (4 / 6) * y)
        Y = round((4 / 3) * y)
        Z = -X - Y
        return Coordinates((X, Y, Z))

    def highlight(self, coordinates: 'Coordinates'):
        """

        :param coordinates:
        :return:
        """
        surface = self.get_surface()
        if coordinates.get_values() in self._map.get_grid().keys():
            hex_size = self._hex_size
            x, y = coordinates.to_cartesian()
            x = x * hex_size - hex_size / 2 + self._size / 2
            y = y * hex_size - hex_size / 2 + self._size / 2
            hex_surface = pygame.transform.scale(Board.images["highlight"], (hex_size, hex_size))
            w, h = hex_surface.get_size()
            x = x - (w - hex_size) / 2
            y = y - (h - hex_size) / 2
            surface.blit(hex_surface, (x, y))
        return surface

