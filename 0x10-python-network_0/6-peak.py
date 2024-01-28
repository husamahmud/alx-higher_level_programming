#!/usr/bin/python3
"""finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers."""
    n = len(list_of_integers)
    if n == 0:
        return None
    elif n == 1:
        return list_of_integers[0]

    l = 0
    r = n - 1
    while l < r:
        m = (l + r) // 2

        if list_of_integers[m] < list_of_integers[m + 1]:
            l = m + 1
        else:
            r = m

    return list_of_integers[l]
