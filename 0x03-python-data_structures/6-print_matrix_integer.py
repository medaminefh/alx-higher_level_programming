#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for cell in row:
            if cell == row[-1]:
                print("{:d}".format(cell), end="")
            else:
                print("{:d} ".format(cell), end="")
        print()
