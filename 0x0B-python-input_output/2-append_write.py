#!/usr/bin/python3
"""A script to appends a string at the end of a text file."""


def append_write(filename="", text=""):
    """Append a string at the end of a text file."""
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
