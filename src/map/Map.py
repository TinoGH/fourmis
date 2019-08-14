
from map.Hexagons import Empty, Edge, Orientation, Ant
import map.coordinates as coords


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
        self._grid[(0, 0, 0)] = Ant(0)
        for i in range(1, radius + 1):
            for j in range(i):
                self._grid[(j, -i, i - j)] = Empty()
                self._grid[(i, j - i, -j)] = Empty()
                self._grid[(i - j, j, -i)] = Empty()
                self._grid[(-j, i, j - i)] = Empty()
                self._grid[(-i, i - j, j)] = Empty()
                self._grid[(j - i, -j, i)] = Empty()
        self._selection = (None, None, None)

    def __str__(self):
        """

        :return:
        """
        string = ""
        for coordinates, cell in self._grid.items():
            string += "{}\t:\t{} \t{}\n".format(coordinates, cell, cell.get_orientation())
        return string

    def get_radius(self):
        """

        :return:
        """
        return self._radius

    def get_grid(self):
        """

        :return:
        """
        return self._grid

    def get_selection(self):
        """

        :return:
        """
        return self._selection

    def get_cell(self, coordinates: (int, int, int)):
        """

        :param coordinates:
        :return:
        """
        if coordinates in self._grid.keys():
            return self._grid[coordinates]
        else:
            return False

    def select(self, coordinates: (int, int, int)):
        """

        :param coordinates:
        :return:
        """
        if coordinates in self._grid.keys():
            self._selection = coordinates
            return True
        else:
            return False

    def deselect(self):
        """

        """
        self._selection = (None, None, None)

    def move_selection(self, direction: int):
        """

        :param direction:
        """
        if self._selection != (None, None, None):
            cell_target_coordinates = coords.look(self._selection, direction)
            if cell_target_coordinates in self._grid.keys():
                if self._grid[cell_target_coordinates].get_name() == "empty":
                    self._grid[cell_target_coordinates] = self._grid[self._selection]
                    self._grid[cell_target_coordinates].set_orientation(direction)
                    self._grid[self._selection] = Empty()
                    self._selection = cell_target_coordinates
            else:
                self._grid[self._selection].set_orientation(direction)
