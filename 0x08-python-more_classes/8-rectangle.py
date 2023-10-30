#!/usr/bin/python3
"""
rectangle module
rectangle class
"""


class Rectangle:
    """ Rectangle class """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ init function
        Args:
        width (int): the width
        height (int): the height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """bigger or equal static method"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __str__(self):
        """str func"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rec = ''
        for row in range(self.__height):
            for col in range(self.__width):
                rec += str(self.print_symbol)
            if row < self.__height - 1:
                rec += "\n"
        return rec

    def __repr__(self):
        """repr func"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """del method"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
