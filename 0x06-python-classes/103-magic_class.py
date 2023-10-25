#!/usr/bin/python3
"""magic class"""
import math


class MagicClass:
    """magic class"""

    def __init__(self, radius=0):
        """init
        Args:
            radius: radius
        """
        self.__radius = 0

        if type(radius) not in (int, float):
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """circumference"""
        return 2 * math.pi * self.__radius
