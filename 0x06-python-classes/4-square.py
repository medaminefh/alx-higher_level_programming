#!/usr/bin/python3
"""Square definition"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """init funtion"""
        self.size = size

    def area(self):
        """area function"""
        return self.size ** 2

    @property
    def size(self):
        """getter size funtion"""
        return self.size

    @size.setter
    def size(self, value):
        """setter size function"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >=0")

        self.size = value
