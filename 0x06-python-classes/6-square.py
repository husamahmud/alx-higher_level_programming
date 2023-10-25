#!/usr/bin/python3
""""Square Class."""


class Square:
    """Square class that defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """"
        Initialize a Square object.

        Agrgs:
            size: The size of the square (Defaults to 0)
            position:

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = size

        if not isinstance(position, tuple) or \
                position[0] < 0 and position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.position = position

    @property
    def size(self):
        """"
        Get the size of the square.

        Returns:
            int: The size of the square
        """
        return self.__size

    @property
    def position(self):
        """
        Get the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @size.setter
    def size(self, value):
        """"
        Set the size of the square

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If the size is not an integer or position is not a tuple
                of 2 positive integers.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if (
                not isinstance(value, tuple)
                or len(value) != 2
                or not isinstance(value[0], int)
                or not isinstance(value[1], int)
                or value[0] < 0 or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
        The position is used to adjust the starting position of the square.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            for _ in range(self.__position[0]):
                print(" ", end="")
            for _ in range(self.__size):
                print("#", end="")
            print()
