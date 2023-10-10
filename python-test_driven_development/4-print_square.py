#!/usr/bin/python3
"""
Module: 4-print_square.py
des: it prints a square based on size
"""


def print_square(size):
    """
    Function that prints a square using '#' based on `size`

    Args:
        size (int): The size of one side of the square.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print('#' * size)
