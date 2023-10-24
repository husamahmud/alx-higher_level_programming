#!/usr/bin/python3
"""Square Class"""


class Square:
    """
    Represents a squars.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
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
        self.size = size
        self.poition = position

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

    @property
    def position(self):
        """
        Get the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(
                isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        Print in stdout the square with the character `#`.
        """
        size = self.size
        if size == 0:
            print()
        else:
            for i in range(size):
                for j in range(size):
                    print('#', end='')
                print()
