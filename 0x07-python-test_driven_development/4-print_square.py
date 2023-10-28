#!/usr/bin/python3

def print_square(size):
    """
    Prints a square with the character `#`.

    Args:
        size (int): The size length of the square.

    Returns:
        None

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than or equal to 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print('#' * size)
