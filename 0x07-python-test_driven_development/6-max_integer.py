#!/usr/bin/python3
"""
This module provides a function for find the max integer in a list
"""


def max_integer(list=[]):
    """
    Finds and returns the maximum integer in a list of integers.

    Args:
        list (list): The list of integers to search for the maximum value. Defaults to an empty list.

    Returns:
        int or None: The maximum integer in the list. If the list is empty, returns None.
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
