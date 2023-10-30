#!/usr/bin/python3
"""Rectangle Class."""


class Rectangle:
    """
    Define the Rectangle Class.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle object.

        Args:
             width (int): The width of the rectangle. Default is 0.
             height (int): The height of the rectangle. Default is 0.

        Raises:
            TypeError (int): If width or height is not an integer.
            ValueError (int): If width or height is less than 0.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: A string representing the rectangle using `print_symbol`
            character. Default is `#`.
        """
        if self.width == 0 or self.height == 0:
            return ""
        else:
            rectangle_str = ''
            for _ in range(self.height - 1):
                rectangle_str += str(self.print_symbol) * self.width + '\n'
            rectangle_str += str(self.print_symbol) * self.width
            return rectangle_str

    def __repr__(self):
        """
        Return a string representation that used to recreate the rectangel.

        Returns:
            str: a string representing the rectangle in the format
            "Rectangle(width, height)"
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Print the message `Bye rectangle...` when an instance is deleted.

        Returns:
            None.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """
        Getter width.

        Returns:
            int: The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, val):
        """
        Setter width.

        Returns:
            int: The width of the rectangle.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        """
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        elif val < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = val

    @property
    def height(self):
        """
        Getter height.

        Returns:
            int: The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, val):
        """
        Setter height.

        Returns:
            int: The height of the rectangle.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        elif val < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = val

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The rectangle perimeter.
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2
