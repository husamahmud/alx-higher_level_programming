#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mtx = []

    for i in matrix:
        new_mtx.append(list(map(lambda n: n * n, i)))

    return new_mtx
