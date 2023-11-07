#!/usr/bin/python3
"""A script to read and print the contents of a file."""


def read_file(filename=""):
    """Read and print the contents of a file."""
    with open(filename, mode='r', encoding='utf-8') as myfile:
        print(myfile.read(), end='')
