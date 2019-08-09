
import pygame
from map.Coordinates import Coordinates


class Hex:
    """

    """
    images_path = "./media/pixel_art/"

    def __init__(self, coordinates: (int, int, int), orientation: int):
        """

        :param coordinates:
        :param orientation:
        """
        assert 0 <= orientation <= 5
        self._coordinates = Coordinates(coordinates)
        self._name = ""
        self._surface = pygame.Surface((256, 256))
        self._orientation = orientation

    def __str__(self):
        """

        :return:
        """
        return self._name

    def get_name(self):
        """

        :return:
        """
        return self._name

    def get_coordinates(self):
        """

        :return:
        """
        return self._coordinates

    def get_orientation(self):
        """

        :return:
        """
        return self._orientation

    def get_surface(self):
        """

        :return:
        """
        return self._surface


class Empty(Hex):
    """

    """
    image = pygame.image.load(Hex.images_path + "empty.png").convert_alpha()

    def __init__(self, coordinates: (int, int, int)):
        """

        :param coordinates:
        """
        super().__init__(coordinates, 0)
        self._name = "Empty"
        self._surface = Empty.image


class Edge(Hex):
    """

    """
    image = pygame.image.load(Hex.images_path + "edge.png").convert_alpha()

    def __init__(self, coordinates: (int, int, int)):
        """

        :param coordinates:
        """
        super().__init__(coordinates, 0)
        self._name = "Edge"
        self._surface = Edge.image


class Orientation(Hex):
    """

    :param orientation:
    """
    image = pygame.image.load(Hex.images_path + "orientation.png").convert_alpha()

    def __init__(self, coordinates: (int, int, int), orientation: int):
        """

        :param coordinates:
        :param orientation:
        """
        super().__init__(coordinates, orientation)
        self._name = "Orientation"
        self._surface = Orientation.image


class Fourmis(Hex):
    """

    :param orientation:
    """
    image = pygame.image.load(Hex.images_path + "fourmis.png").convert_alpha()

    def __init__(self, coordinates: (int, int, int), orientation: int):
        """

        :param coordinates:
        :param orientation:
        """
        super().__init__(coordinates, orientation)
        self._name = "Fourmis"
        self._surface = Fourmis.image

    def set_orientation(self, orientation):
        """

        :param orientation:
        :return:
        """
        self._orientation = orientation
