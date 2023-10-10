#!/usr/bin/python3
"""
Module Name: 0-add_integer.py
des: defines as integer addition function
function name: add_integer()
"""


def add_integer(a, b=98):
    """
    add_integer: adds integers and floats

    Args:
    a(int): First value
    b (int, optional): second value defaults to 98

    Returns:
     int: the sum of a and b
    """
    if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")

    if b is None or (type(b) is not int and type(b) is not float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
