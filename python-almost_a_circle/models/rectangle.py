#!/usr/bin/python3
from models.base import Base
""" New Rectangle Class """


class Rectangle(Base):
    """ Rectangle class that inherits from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize the rectangle instance"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """ Width Getter and Setter"""
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    """ Height Getter and Setter"""
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    """ x Getter and Setter"""
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    """ y Getter and Setter"""
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
