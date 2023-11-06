#!/usr/bin/python3
"""MyList Class."""


class MyList(list):
    """MyList class that defines a class that inherits from list."""

    def __init__(self):
        """Initialize a MyList object"""
        list.__init__(self, [])

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)."""
        sorted_list = sorted(self)
        print(sorted_list)
