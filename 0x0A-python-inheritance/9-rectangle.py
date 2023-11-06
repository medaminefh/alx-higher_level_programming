#!/usr/bin/python3
"""lockedclass module"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """LockedClass"""
    def __init__(self, width, height):
        """init function"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """return the area"""
        return self.__width * self.__height

    def __str__(self):
        """return the description"""
        out = f"[Rectangle] {self.__width}/{self.__height}"
        return out
