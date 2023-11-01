#!/usr/bin/python3
"""
This module provides a function for reformat text
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: `.` `?` `:`.

    Args:
        text (str): The input text to be processed and printed.

    Returns:
        None

    Raises:
        TypeError: If the input `text` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    special_chars = ['.', '?', ':']
    lines = []
    curr_line = ''

    for char in text:
        curr_line += char
        if char in special_chars:
            lines.append(curr_line.strip())
            lines.append('')
            curr_line = ''

    if curr_line:
        lines.append(curr_line.strip())
    for line in lines:
        print(line)
