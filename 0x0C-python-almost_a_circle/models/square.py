#!/usr/bin/python3
"""Square Class"""

from .rectangle import Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square object."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """Getter size."""
        return self.width

    @size.setter
    def size(self, val):
        """Setter size."""
        self.__height = val
        self.__width = val

    def area(self):
        """Calculate the area of the square."""
        return self.width ** 2

    def display(self):
        """Print a square with the character `#`"""
        for _ in range(self.height):
            print()

        for _ in range(self.size):
            for _ in range(self.width):
                print(" ", end="")
            print('#' * self.size, end='')
            print()

    def update(self, *args, **kwargs):
        """Update the attributes of the Square object with given args"""
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            for key, value in kwargs.items():
                self.__setattr__(key, value)

    def to_dictionary(self):
        """Returns a dictionary representation of the square obj"""
        return {
            'id': getattr(self, 'id'),
            'size': getattr(self, 'size'),
            'x': getattr(self, 'x'),
            'y': getattr(self, 'y')
        }
