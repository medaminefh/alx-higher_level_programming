#!/usr/bin/python3
"""
print_square  module
print_square func
"""


def print_square(size):
    """print_square function"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
