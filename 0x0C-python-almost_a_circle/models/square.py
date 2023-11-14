#!/usr/bin/python3
"""lockedclass module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class that inherits from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """init function"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """return the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for the value"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """the update function that updates the instance"""
        if args and len(args) > 0:
            i = 0
            for arg in args:
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """str function"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        """return a json repr of the instance"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
