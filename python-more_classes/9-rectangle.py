#!/usr/bin/python3
"""
New class for Rectangle
"""


class Rectangle:
    """ Rectangle Class based on 8-rectangle """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    """ Width """
    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """ Height """
    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    """ Area of Rectangle """
    def area(self):
        return self.width * self.height

    """ Perimeter of Rectangle"""
    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    """ Print Rectangle using # """
    def __str__(self):
        empty_string = ""
        if self.__width == 0 or self.__height == 0:
            return (empty_string)
        symbol_str = str(self.print_symbol)
        return (((symbol_str * self.width) + "\n") * self.height)[:-1]

    """ Returns 'official' string rep of an instance"""
    def __repr__(self):
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    """ Print a message when the instance is deleted """
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    """ Returns biggest rectangle according to its area"""
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() == rect_2.area():
            return rect_1
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
    """ Returns new rectangle instance with width == height == size"""
    @classmethod
    def square(cls, size=0):
        return cls(size, size)
