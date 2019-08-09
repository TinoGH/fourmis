
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
        for i in range(radius + 2):
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
