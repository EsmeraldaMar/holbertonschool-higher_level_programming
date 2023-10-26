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
    @property
    def size(self):
        """ Retrieves itself"""
        return self.width

    @size.setter
    def size(self, value):
        """ Inherits from rectangle"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute"""
        if args:
            for arguments in range(len(args)):
                if arguments == 0:
                    self.id = args[arguments]
                if arguments == 1:
                    self.size = args[arguments]
                if arguments == 2:
                    self.x = args[arguments]
                if arguments == 3:
                    self.y = args[arguments]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Dictionary represenation for class Square"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
