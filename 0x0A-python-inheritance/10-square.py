#!/usr/bin/python3
"""lockedclass module"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """LockedClass"""
    def __init__(self, size):
        """init function"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
