#!/usr/bin/python3
""""Square Class."""


class Square:
    """Square class that defines a square."""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size ** 2
