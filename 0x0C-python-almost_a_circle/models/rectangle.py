#!/usr/bin/python3
"""Rectangle Class"""

from .base import Base


class Rectangle(Base):
    """Represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle instance."""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter width"""
        return self.__width

    @width.setter
    def width(self, val):
        """Setter width"""
        if not isinstance(val, int):
            raise TypeError('width must be an integer')
        if val <= 0:
            raise ValueError('width must be > 0')
        self.__width = val

    @property
    def height(self):
        """Getter height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter height"""
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        """Getter x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter x"""
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        """Getter y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Setter y"""
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def __str__(self):
        """Return a string representation of the object."""
        return (f"[Rectable] ({self.id}) {self.x}/{self.y} "
                f"- {self.width}/{self.height}")

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print a rectangle with the character `#`"""
        for _ in range(self.y):
            print()

        for _ in range(self.height):
            for _ in range(self.x):
                print(" ", end="")
            print('#' * self.width, end='')
            print()

    def update(self, *args, **kwargs):
        """Update the attributes of the Rectangle object with given args"""
        if args:
            attr_names = ['id', 'width', 'height', 'x', 'y']
            for arg, attr in zip(args, attr_names):
                setattr(self, attr, arg)
        elif kwargs:
            for attr, val in kwargs.items():
                setattr(self, attr, val)

    def to_dictionary(self):
        """Returns a dictionary representation of the square obj"""
        return {
            'id': getattr(self, 'id'),
            'width': getattr(self, 'width'),
            'height': getattr(self, 'id'),
            'x': getattr(self, 'x'),
            'y': getattr(self, 'y')
        }
