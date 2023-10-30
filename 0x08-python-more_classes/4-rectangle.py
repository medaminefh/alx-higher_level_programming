#!/usr/bin/python3
"""
rectangle module
rectangle class
"""


class Rectangle:
    """ Rectangle class """

    def __init__(self, width=0, height=0):
        """ init function
        Args:
        width (int): the width
        height (int): the height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """property width"""
        return self.__width

    @property
    def height(self):
        """prop height"""
        return self.__height

    @width.setter
    def width(self, value):
        """set the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """set the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*(self.__height + self.__width)

    def __str__(self):
        """str func"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rec = ''
        for row in range(self.__height):
            for col in range(self.__width):
                rec += "#"
            if row < self.__height - 1:
                rec += "\n"
        return rec

    def __repr__(self):
        """repr func"""
        return f"Rectangle({self.__width}, {self.__height})"
