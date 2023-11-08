#!/usr/bin/python3
"""Myint class"""


class MyInt(int):
    """MyInt class"""

    def __eq__(self, value):
        """override =="""
        return self.real != value

    def __ne__(self, value):
        """override !="""
        return self.real == value
