#!/usr/bin/python3
""" New Rectangle Class """
from models.base import Base


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
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    """ Height Getter and Setter"""
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    """ x Getter and Setter"""
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    """ y Getter and Setter"""
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    """ Public Methods"""
    def area(self):
        """ Return the area value of the Rectangle instance """
        return (self.__width * self.__height)

    def display(self):
        """ Prints in stdout the Rectangle instance with the character #"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            for _ in range(self.__x):
                print(" ", end="")
            for _ in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute"""
        if args:
            for arguments in range(len(args)):
                if arguments == 0:
                    self.id = args[arguments]
                if arguments == 1:
                    self.width = args[arguments]
                if arguments == 2:
                    self.height = args[arguments]
                if arguments == 3:
                    self.x = args[arguments]
                if arguments == 4:
                    self.y = args[arguments]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """ Returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return ("[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}".
                format(self.id, self.__x,
                       self.__y, self.__width, self.__height))

    def to_dictionary(self):
        """ Returns the dictionary representation of a Rectangle"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
            }
