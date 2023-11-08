#!/usr/bin/python3
"""class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square"""

    def __init__(self, size):
        """init the square"""
        self.__size = size
        super().integer_validator("size", size)

    def area(self):
        """area of the square"""
        return self.__size * self.__size
