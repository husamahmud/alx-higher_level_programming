#!/usr/bin/python3
def lookup(obj):
    """Return a list of attributes & methods available for the given object."""
    return dir(obj)
