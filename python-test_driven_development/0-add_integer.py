#!/usr/bin/python3
"""
Module Name: 0-add_integer.py
des: defines as integer addition function
function name: add_integer()
"""


def add_integer(a, b=98):
    """
    add_integer: adds integers and returns the sum
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if (a == float('NaN')):
        raise ValueError("can't convert NaN to integer")
    return (int(a) + int(b))


if __name__ == "__main__":
    import doctest
    doctest.testfile('tests/0-add_integer.txt')
