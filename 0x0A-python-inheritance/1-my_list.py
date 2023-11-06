#!/usr/bin/python3
"""MyList Class."""


class MyList(list):
    """MyList class that defines a class that inherits from list."""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)."""
        print(sorted(self))
