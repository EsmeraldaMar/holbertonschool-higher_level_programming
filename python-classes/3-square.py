#!/usr/bin/python3
"""It defines class square"""


class Square:
    """
    Class that defines properties of square based on 1-square
    """
    def __init__(self, size=0):
        """Initialise new square
            Args:
                size(int): size of new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return (self.__size * self.__size)
