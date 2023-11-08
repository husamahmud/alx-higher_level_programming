#!/usr/bin/python3
"""
A script to returns the dictionary description with simple data structure
for JSON serialization of an object
"""


def class_to_json(obj):
    """Convert an object to a dictionary representation."""
    return obj.__dict__
