#!/usr/bin/python3
"""Square definition"""


class Square:
    """Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """init funtion"""
        self.__size = size
        self.__position = position

    def area(self):
        """area function"""
        return self.__size ** 2

    def my_print(self):
        """print function"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for k in range(self.__size):
                print("#", end="")
            print()

    @property
    def size(self):
        """getter size funtion"""
        return self.__size

    @property
    def position(self):
        """getter position"""
        return self.__position

    @position.setter
    def position(self, v):
        """setter position"""
        if not isinstance(value, tuple) or not v[0] >= 0 or not v[1] >= 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    @size.setter
    def size(self, value):
        """setter size function"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >=0")

        self.__size = value
