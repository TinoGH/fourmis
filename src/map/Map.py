
import pygame
from math import floor
from map.Hex import *


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
        self._grid[(0, 0, 0)] = Orientation((0, 0, 0), 2)
        for i in range(1, radius + 2):
            if i < radius + 1:
                cell = Empty
            else:
                cell = Edge
            for j in range(i):
                self._grid[(j, -i, i - j)] = cell((j, -i, i - j))
                self._grid[(i, j - i, -j)] = cell((i, j - i, -j))
                self._grid[(i - j, j, -i)] = cell((i - j, j, -i))
                self._grid[(-j, i, j - i)] = cell((-j, i, j - i))
                self._grid[(-i, i - j, j)] = cell((-i, i - j, j))
                self._grid[(j - i, -j, i)] = cell((j - i, -j, i))

    def __str__(self):
        """

        :return:
        """
        string = ""
        for cell in self._grid.values():
            string += "{}\t:\t{} \t{}\n".format(cell.get_coordinates(), cell, cell.get_orientation())
        return string

    def get_surface(self, size):
        """

        :return:
        """
        surface = pygame.Surface((size, size))
        surface.fill([255, 255, 255])
        hex_size = floor(size / (2 * (self._radius + 1) + 1))
        for cell in self._grid.values():
            x, y = cell.get_coordinates().to_cartesian()
            x = x * hex_size - hex_size / 2 + size / 2
            y = y * hex_size - hex_size / 2 + size / 2
            hex_surface = pygame.transform.rotate(
                pygame.transform.scale(cell.get_surface(), (hex_size, hex_size)),
                cell.get_orientation() * 60)
            w, h = hex_surface.get_size()
            x = x - (w - hex_size) / 2
            y = y - (h - hex_size) / 2
            surface.blit(hex_surface, (x, y))
        return surface
