
from math import sqrt


class Coordinates:
    """

    """

    def __init__(self, x: int, y: int, z: int):
        """

        :param x:
        :param y:
        :param z:
        """
        assert (x + y + z) == 0
        self._x = x
        self._y = y
        self._z = z

    def __str__(self):
        """

        :return:
        """
        return "({}, {}, {})".format(self._x, self._y, self._z)

    def to_cartesian(self):
        """

        :return:
        """
        x = sqrt(3) / 2 * (self._x + self._y / 2)
        y = 3 / 4 * self._y
        return x, y

    def neighbours(self):
        """

        :return:
        """
        return [
            Coordinates(self._x, self._y + 1, self._z - 1),
            Coordinates(self._x, self._y - 1, self._z + 1),
            Coordinates(self._x + 1, self._y, self._z - 1),
            Coordinates(self._x - 1, self._y, self._z + 1),
            Coordinates(self._x + 1, self._y - 1, self._z),
            Coordinates(self._x - 1, self._y + 1, self._z),
        ]
