#!/usr/bin/python3
"""Square class definition"""


class Square:
    """square class"""
    def __init__(self, size=0):
        """ __init__ function
        Args:
            size (int): the size of the squre
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.__size = size
