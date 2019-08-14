
from math import sqrt

ORIENTATIONS = [
    (1, 0, -1),
    (1, -1, 0),
    (0, -1, 1),
    (-1, 0, 1),
    (-1, 1, 0),
    (0, 1, -1)
]

ORIENTATIONS_NAMES = [
    "East",
    "North-East",
    "North-West",
    "West",
    "South-West",
    "South-East"
]


def to_cartesian(coordinates: (int, int, int)):
    """

    :param coordinates:
    :return:
    """
    X, Y, Z = coordinates
    x = sqrt(3) / 2 * (X + Y / 2)
    y = 3 / 4 * Y
    return x, y


def from_cartesian(cartesian: (int, int)):
    """

    :param cartesian:
    :return:
    """
    x, y = cartesian
    X = round((2 / sqrt(3)) * x - (4 / 6) * y)
    Y = round((4 / 3) * y)
    Z = -X - Y
    return X, Y, Z


def neighbours(coordinates: (int, int, int)):
    """

    :param coordinates
    :return:
    """
    X, Y, Z = coordinates
    return [(X + Xd, Y + Yd, Z + Zd) for (Xd, Yd, Zd) in ORIENTATIONS]


def look(coordinates: (int, int, int), direction: int):
    """

    :param coordinates:
    :param direction:
    :return:
    """
    assert 0 <= direction <= 5
    X, Y, Z = coordinates
    Xd, Yd, Zd = ORIENTATIONS[direction]
    return X + Xd, Y + Yd, Z + Zd
