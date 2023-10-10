#!/usr/bin/python3
"""
Module Name: 2-matrix_divided.py
des: divides all elements of a matrix
function name: matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """
    matrix_divided: takes a matrix and divides the values by 'div'
    div (int or float): divisor

    Args:
    matrix: matrix to be divided
    div: division

    Returns:
     new matrix with divided of all elements in a matrix
    """
    row_len = -1
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list or len(matrix) is 0:
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    new_matrix = []
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix "
                            "(list of lists) of integers/floats")
        if row_len == -1:
            row_len = len(row)
            if row_len == 0:
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
        else:
            if row_len is not len(row):
                raise TypeError("Each row of the matrix "
                                "must have the same size")
        new_row = []
        for e in row:
            if type(e) is int or type(e) is float:
                new_row.append(round(e / div, 2))
            else:
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
        new_matrix.append(new_row)
    return new_matrix
