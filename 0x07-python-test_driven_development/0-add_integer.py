#!/usr/bin/python3


def add_integer(a, b=98):
    """
    Adds 2 integers.

    Args:
        a (int, flaot): The first integer.
        b (int, flaot): The second integer. Defaults to 98.

    Returns:
        int: The sum of the two integers.

    Raises:
        TypeError: If either `a` or `b` is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    return int(a) + int(b)
