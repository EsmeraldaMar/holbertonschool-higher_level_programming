#!/usr/bin/python3
"""
This module contains one function for adding 2 integers together
"""


def add_integer(a, b=98):
    """
    Sums up the arguments passed in.
    Args:
        a (int) : first one
        b (int) : second one (default value 98)
    Returns:
        int: sum of a and b
    """
    if a is None or (isinstance(a, int) is not True and isinstance(a, float) is not True):
        raise TypeError("a must be an integer")
    if b is None or (isinstance(b, int) is not True and isinstance(b, float) is not True):
        raise TypeError("b must be an integer")
    #if (a == float('NaN')):
        #raise ValueError("can't convert NaN to integer")
    # if isinstance(a, float):
    #     a = int(a)
    # if isinstance(b, float):
    #     b = int(b)
    return int(a) + int(b)
