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
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
