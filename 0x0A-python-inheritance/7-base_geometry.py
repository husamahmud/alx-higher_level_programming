#!/usr/bin/python3
"""class BaseGeometry"""


class BaseGeometry:
    """empty class """

    def area(self):
        """area of the shape"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate name and value
        Args:
            name (str): name
            value (int): value
        Raise:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to 0
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
