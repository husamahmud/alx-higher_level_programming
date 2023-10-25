#!/usr/bin/python3
""""Square Class."""


class Square:
    """Square class that defines a square."""

    def __init__(self, size=0):
        """"
        Initialize a Square object.

        Agrgs:
            size: The size of the square (Defaults to 0)

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """"
        Get the size of the square.

        Returns:
            int: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """"
        Set the size of the square

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print a square with the character `#`

        If the size of the Square is 0, an empty line is printed.
        """
        size = self.size
        if size == 0:
            print()
            return

        for _ in range(size):
            for _ in range(size):
                print('#', end='')
            print()
