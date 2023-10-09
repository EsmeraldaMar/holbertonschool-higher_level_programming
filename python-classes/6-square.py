#!/usr/bin/python3
"""It defines class square"""


class Square:
    """
    Class that defines properties of square based on 5-square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialise new square
            Args:
                size(int): size of new square
                position(tuple): coordinate of the new square
        """
        self.size = size
        self.position = position

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(n, int)  for n in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.size):
                print('#' * self.size)
