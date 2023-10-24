#!/usr/bin/python3
"""Square Class"""


class Square:
    """
    Represents a squars.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initialize a square with the given size.

        Args:
            size (int): The size of the squarse. Defaults to 0.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is negative.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """
        Calculate the area of the size.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Get the size of square.

        Return:
              int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new sizs of the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the  size is negative.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
