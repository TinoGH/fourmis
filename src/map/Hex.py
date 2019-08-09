
import pygame


class Hex:
    """

    """

    def __init__(self):
        """

        """
        self._name = ""
        self._surface = pygame.Surface((256, 256))

    def __str__(self):
        """

        :return:
        """
        return self._name

    def get_surface(self):
        """

        :return:
        """
        return self._surface


class Empty(Hex):
    """

    """

    def __init__(self):
        """

        """
        super().__init__()
        self._name = "Empty"
        self._surface = pygame.image.load("./media/pixel_art/empty.png").convert_alpha()


class Edge(Hex):
    """

    """

    def __init__(self):
        """

        """
        super().__init__()
        self._name = "Edge"
        self._surface = pygame.image.load("./media/pixel_art/edge.png").convert_alpha()
