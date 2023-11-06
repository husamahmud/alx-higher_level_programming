#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Return a list of attributes & methods available for the given object."""
    return dir(obj)
