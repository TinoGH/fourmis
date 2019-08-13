
from map.Coordinates import Coordinates


class Hex:
    """

    """
    hex_list = [
        "empty",
        "edge",
        "orientation",
        "ant",
        "highlight"
    ]

    def __init__(self, coordinates: (int, int, int), orientation: int):
        """

        :param coordinates:
        :param orientation:
        """
        assert 0 <= orientation <= 5
        self._coordinates = Coordinates(coordinates)
        self._name = ""
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

    def set_orientation(self, orientation):
        """

        :param orientation:
        :return:
        """
        self._orientation = orientation


class Empty(Hex):
    """

    """

    def __init__(self, coordinates: (int, int, int)):
        """

        :param coordinates:
        """
        super().__init__(coordinates, 0)
        self._name = "empty"


class Edge(Hex):
    """

    """

    def __init__(self, coordinates: (int, int, int)):
        """

        :param coordinates:
        """
        super().__init__(coordinates, 0)
        self._name = "edge"


class Orientation(Hex):
    """

    :param orientation:
    """

    def __init__(self, coordinates: (int, int, int), orientation: int):
        """

        :param coordinates:
        :param orientation:
        """
        super().__init__(coordinates, orientation)
        self._name = "orientation"


class Ant(Hex):
    """

    :param orientation:
    """

    def __init__(self, coordinates: (int, int, int), orientation: int):
        """

        :param coordinates:
        :param orientation:
        """
        super().__init__(coordinates, orientation)
        self._name = "ant"
