

class Hex:
    """

    """

    def __init__(self):
        """

        """
        self._name = ""

    def __str__(self):
        """

        :return:
        """
        return self._name


class Empty(Hex):
    """

    """

    def __init__(self):
        """

        """
        super().__init__()
        self._name = "Empty"


class Edge(Hex):
    """

    """

    def __init__(self):
        """

        """
        super().__init__()
        self._name = "Edge"
