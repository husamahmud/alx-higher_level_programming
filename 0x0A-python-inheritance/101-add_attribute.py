#!/usr/bin/python3
"""add a new attri if valid"""


def add_attribute(obj, att, value):
    """add a new attribute and a value if valid"""
    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
