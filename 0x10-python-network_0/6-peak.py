#!/usr/bin/python3
"""finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers."""
    n = len(list_of_integers)
    if n == 0:
        return None

    left = 0
    right = n - 1
    while left < right:
        m = (left + right) // 2

        if list_of_integers[m] < list_of_integers[m + 1]:
            left = m + 1
        else:
            right = m

    return list_of_integers[left]
