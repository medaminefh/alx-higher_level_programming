#!/usr/bin/python3
"""
0-add_integer module
add_integer function adds two integers
"""


def add_integer(a, b=98):
    """Add function"""

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
