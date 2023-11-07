#!/usr/bin/python3
"""A script to writes a string to a text file."""


def write_file(filename="", text=""):
    """Writes a string to a text file."""
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
