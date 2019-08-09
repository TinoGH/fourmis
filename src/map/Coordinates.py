
from math import sqrt


class Coordinates:
    """

    """
    directions = [
        (1, 0, -1),
        (1, -1, 0),
        (0, -1, 1),
        (-1, 0, 1),
        (-1, 1, 0),
        (0, 1, -1)
    ]

    def __init__(self, coordinates: (int, int, int)):
        """

        :param x:
        :param y:
        :param z:
        """
        x, y, z = coordinates
        assert (x + y + z) == 0
        self._x = x
        self._y = y
        self._z = z

    def __str__(self):
        """

        :return:
        """
        return "({}, {}, {})".format(self._x, self._y, self._z)

    def get_values(self):
        """

        :return:
        """
        return self._x, self._y, self._z

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

    def look(self, direction):
        """

        :param direction:
        :return:
        """
        assert 0 <= direction <= 5
        return (
            self._x + Coordinates.directions[direction][0],
            self._y + Coordinates.directions[direction][1],
            self._z + Coordinates.directions[direction][2]
        )

    def move(self, direction):
        """

        :param direction:
        :return:
        """
        assert 0 <= direction <= 5
        self._x += Coordinates.directions[direction][0]
        self._y += Coordinates.directions[direction][1]
        self._z += Coordinates.directions[direction][2]
