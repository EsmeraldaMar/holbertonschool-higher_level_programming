#!/usr/bin/python3
""" New class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """ Class Constructor"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ Returns [Square] (<id>) <x>/<y> - <width>/<height>"""
        return ("[{}] ({}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x,
            self.y, self.size))

    """ Public, Size Getter and Setters"""
    def size(self):
        return self.width

    def size(self, value):
        self.width = value
        self.height = value
