#!/usr/bin/python3
"""
This module provides a function for dividing elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int): The divisor.

    Returns:
        list: A new matrix with each element divided by the divisor.

    Raises:
        TypeError: If the matrix is not a valid matrix of integers/floats,
            or if the divisor is not a number (integer or float).
        ZeroDivisionError: If the divisor is zero.
    """
    n = len(matrix[0])

    for row in matrix:
        for val in row:
            if not isinstance(val, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        if len(row) != n:
            raise TypeError("Each row of the matrix must have the same size")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    new_matrix = []

    for rows in matrix:
        new_row = []
        for num in rows:
            val = round(num / div, 2)
            new_row.append(val)
        new_matrix.append(new_row)

    return new_matrix
