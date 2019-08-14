
import pygame
from map.Map import Map
from map.Hexagons import Hexagon
from math import floor
import map.coordinates as coords


class Board:
    """

    """

    images_path = "./media/pixel_art/"
    images = dict()
    for hex_type in Hexagon.hexagons_list:
        images[hex_type] = pygame.image.load(images_path + hex_type + ".png").convert_alpha()

    def __init__(self, size: int, map: 'Map'):
        """

        :param size:
        :param map:
        """
        self._size = size
        self._map = map
        self._hex_size = floor(size / (2 * self._map.get_radius() + 1))
        self._base_surface = pygame.Surface((size, size))
        self._base_surface.fill([255, 255, 255])
        for coordinates, cell in self._map.get_grid().items():
            hexagon = pygame.transform.scale(Board.images["hexagon"], (self._hex_size, self._hex_size))
            x_pixels, y_pixels = self.cartesian_to_pixels(coords.to_cartesian(coordinates), hexagon.get_size())
            self._base_surface.blit(hexagon, (x_pixels, y_pixels))
        self._surface = pygame.Surface((size, size))
        self.update_surface()

    def update_surface(self):
        """

        """
        self._surface.fill([255, 255, 255])
        self._surface.blit(self._base_surface, (0, 0))
        for coordinates, cell in self._map.get_grid().items():
            hex_surface = pygame.transform.rotate(
                pygame.transform.scale(Board.images[cell.get_name()], (self._hex_size, self._hex_size)),
                cell.get_orientation() * 60)
            x_pixels, y_pixels = self.cartesian_to_pixels(coords.to_cartesian(coordinates), hex_surface.get_size())
            self._surface.blit(hex_surface, (x_pixels, y_pixels))

    def get_surface(self):
        """

        :return:
        """
        return self._surface

    def pixels_to_coordinates(self, pixels: (int, int)):
        """

        :param pixels:
        :return:
        """
        x_pixels, y_pixels = pixels
        x, y = (x_pixels - self._size / 2) / self._hex_size, (y_pixels - self._size / 2) / self._hex_size
        return x, y

    def cartesian_to_pixels(self, cartesian: (int, int), size: (int, int)):
        """

        :param cartesian:
        :param size:
        :return:
        """
        x, y = cartesian
        width, height = size
        x_pixels = self._hex_size * (x - 1 / 2) + self._size / 2 - (width - self._hex_size) / 2
        y_pixels = self._hex_size * (y - 1 / 2) + self._size / 2 - (height - self._hex_size) / 2
        return x_pixels, y_pixels

    def highlight(self, coordinates: (int, int, int)):
        """

        :param coordinates:
        """
        if coordinates in self._map.get_grid().keys():
            highlight = pygame.transform.scale(Board.images["highlight"], (self._hex_size, self._hex_size))
            x_pixels, y_pixels = self.cartesian_to_pixels(coords.to_cartesian(coordinates), highlight.get_size())
            self._surface.blit(highlight, (x_pixels, y_pixels))
