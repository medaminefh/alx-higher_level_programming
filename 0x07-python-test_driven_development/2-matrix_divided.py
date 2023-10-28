#!/usr/bin/python3
"""
1-matrix  module
matrix_divided func
"""


def matrix_divided(matrix, div):
    """matrix function"""
    typerror = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) is not list:
        raise TypeError(typerror)
    length = 0
    out = []

    for row in range(len(matrix)):
        if type(matrix[row]) is not list:
            raise TypeError(typerror)
        if length == 0:
            length = len(matrix[row])
        elif length != len(matrix[row]):
            raise TypeError("Each row of the matrix must have the same size")
        out.append([])
        for cell in range(len(matrix[row])):
            if type(matrix[row][cell]) not in [int, float]:
                raise TypeError(typerror)
            elif type(div) not in [int, float]:
                raise TypeError("div must be a number")
            elif div == 0:
                raise ZeroDivisionError("division by zero")
            else:
                out[row].append(round((matrix[row][cell] / div), 2))
    return out
