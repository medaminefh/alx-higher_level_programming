#!/usr/bin/python3
"""Square definition"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """init funtion"""
        self.__size = size

    def area(self):
        """area function"""
        return self.__size ** 2

    def my_print(self):
        """print function"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for i in range(self.__size):
                print("#", end="")
            print()

    @property
    def size(self):
        """getter size funtion"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter size function"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >=0")

        self.__size = value
