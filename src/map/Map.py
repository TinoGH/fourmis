
from map.Hex import Empty, Edge, Orientation, Ant


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
        self._grid[(0, 0, 0)] = Ant((0, 0, 0), 0)
        for i in range(1, radius + 2):
            if i < radius + 1:
                cell = Empty
            else:
                cell = Edge
            for j in range(i):
                self._grid[(j, -i, i - j)] = cell((j, -i, i - j))
                self._grid[(i, j - i, -j)] = cell((i, j - i, -j))
                self._grid[(i - j, j, -i)] = cell((i - j, j, -i))
                self._grid[(-j, i, j - i)] = cell((-j, i, j - i))
                self._grid[(-i, i - j, j)] = cell((-i, i - j, j))
                self._grid[(j - i, -j, i)] = cell((j - i, -j, i))
        self._selection = (0, 0, 0)

    def __str__(self):
        """

        :return:
        """
        string = ""
        for cell in self._grid.values():
            string += "{}\t:\t{} \t{}\n".format(cell.get_coordinates(), cell, cell.get_orientation())
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

    def move_selection(self, direction: int):
        """

        :param direction:
        """
        cell_target_coordinates = self._grid[self._selection].get_coordinates().look(direction)
        if self._grid[cell_target_coordinates].get_name() == "empty":
            self._grid[cell_target_coordinates] = self._grid[self._selection]
            self._grid[cell_target_coordinates].get_coordinates().move(direction)
            self._grid[cell_target_coordinates].set_orientation(direction)
            self._grid[self._selection] = Empty(self._selection)
            self._selection = cell_target_coordinates
            print("moved to {}".format(cell_target_coordinates))
        else:
            self._grid[self._selection].set_orientation(direction)
            print("stay at {}".format(self._selection))
