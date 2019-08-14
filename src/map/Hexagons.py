

class Hexagon:
    """

    """
    hexagons_list = [
        "hexagon",
        "highlight",
        "empty",
        "edge",
        "orientation",
        "ant"
    ]

    def __init__(self, orientation: int):
        """

        :param orientation:
        """
        assert 0 <= orientation <= 5
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


class Empty(Hexagon):
    """

    """

    def __init__(self):
        """

        """
        super().__init__(0)
        self._name = "empty"


class Edge(Hexagon):
    """

    """

    def __init__(self):
        """

        """
        super().__init__(0)
        self._name = "edge"


class Orientation(Hexagon):
    """

    :param orientation:
    """

    def __init__(self, orientation: int):
        """

        :param orientation:
        """
        super().__init__(orientation)
        self._name = "orientation"


class Ant(Hexagon):
    """

    :param orientation:
    """

    def __init__(self, orientation: int):
        """

        :param orientation:
        """
        super().__init__(orientation)
        self._name = "ant"
