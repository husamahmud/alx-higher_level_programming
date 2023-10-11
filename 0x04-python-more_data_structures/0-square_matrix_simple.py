#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []

    for row in range(3):
        new_row = []
        for col in range(3):
            new_row.append(matrix[row][col] ** 2)
        new_matrix.append(new_row)

    return new_matrix
