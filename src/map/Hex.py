
import pygame


class Hex:
    """

    """

    def __init__(self, image_path: str, orientation: int):
        """

        :param image_path:
        :param orientation:
        """
        assert 0 <= orientation <= 5
        self._name = ""
        self._surface = pygame.image.load(image_path).convert_alpha()
        self._orientation = orientation

    def __str__(self):
        """

        :return:
        """
        return self._name

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

    def __init__(self):
        """

        """
        super().__init__("./media/pixel_art/empty.png", 0)
        self._name = "Empty"


class Edge(Hex):
    """

    """

    def __init__(self):
        """

        """
        super().__init__("./media/pixel_art/edge.png", 0)
        self._name = "Edge"


class Orientation(Hex):
    """

    :param orientation:
    """

    def __init__(self, orientation: int):
        """

        """
        super().__init__("./media/pixel_art/orientation.png", orientation)
        self._name = "Orientation"
