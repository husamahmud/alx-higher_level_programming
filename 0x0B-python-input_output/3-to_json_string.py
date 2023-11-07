#!/usr/bin/python3
"""A script to return the JSON representation of an object"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object."""
    return json.dumps(my_obj)
