"""Functions to calculate grains on a chessboard."""

def square(number):
    """Calculate the number of grains on a given square.
    :param number: int - number of square.
    :return: int - number of grains.
    """
    if (number<=0 or number >64):
        raise ValueError("square must be between 1 and 64")
    return 2**(number-1)

def total():
    """Calculate the total of squares and grains.
    :return: int - total of grains on the chessboard.
    """
    return 2**64-1