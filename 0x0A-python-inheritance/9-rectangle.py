#!/usr/bin/python3
"""Rectangle class"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """init the height and width"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """the area of the rectangle"""
        return self.__height * self.__width

    def __str__(self):
        """print format of the rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
