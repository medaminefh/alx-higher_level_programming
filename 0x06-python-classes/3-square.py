#!/usr/bin/python3
"""Square class"""


class Square:
    """class defintion"""
    def __init__(self, size=0):
        """
        Init function

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.__size = size

    def area(self):
        """area function"""
        return self.__size ** 2
