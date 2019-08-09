
import pygame
from math import floor
from map.Hex import Empty, Edge
from map.Coordinates import Coordinates


class Map:
    """

    """

    def __init__(self, radius: int):
        """

        :param radius:
        """
        assert radius >= 0
        self._radius = radius
        self._grid = dict()
        self._grid[Coordinates(0, 0, 0)] = Empty()
        for i in range(1, radius + 2):
            if i < radius + 1:
                cell = Empty
            else:
                cell = Edge
            for j in range(i):
                self._grid[Coordinates(j, -i, i - j)] = cell()
                self._grid[Coordinates(i, j - i, -j)] = cell()
                self._grid[Coordinates(i - j, j, -i)] = cell()
                self._grid[Coordinates(-j, i, j - i)] = cell()
                self._grid[Coordinates(-i, i - j, j)] = cell()
                self._grid[Coordinates(j - i, -j, i)] = cell()

    def __str__(self):
        """

        :return:
        """
        string = ""
        for coordinates in self._grid.keys():
            string += "{}\t:\t{}\n".format(coordinates, self._grid[coordinates])
        return string

    def get_surface(self, size):
        """

        :return:
        """
        surface = pygame.Surface((size, size))
        surface.fill([255, 255, 255])
        hex_size = floor(size / (2 * (self._radius + 1) + 1))
        for coordinates in self._grid.keys():
            x, y = coordinates.to_cartesian()
            x = round(x * hex_size - hex_size / 2 + size / 2)
            y = round(y * hex_size - hex_size / 2 + size / 2)
            hex_surface = pygame.transform.scale(self._grid[coordinates].get_surface(), (hex_size, hex_size))
            surface.blit(hex_surface, (x, y))
        return surface
