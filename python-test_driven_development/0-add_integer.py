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
    returns the sum
    """
    if a is None or (isinstance(a, int) is not True and isinstance(a, float) is not True):
        raise TypeError("a must be an integer")
    if b is None or (isinstance(b, int) is not True and isinstance(b, float) is not True):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
