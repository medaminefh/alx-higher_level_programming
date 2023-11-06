#!/usr/bin/python3
"""lockedclass module"""


class BaseGeometry:
    """LockedClass"""

    def area(self):
        """area instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validator"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
