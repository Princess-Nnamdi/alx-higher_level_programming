#!/usr/bin/python3
# 2-matrix_divided.py
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists of int/float): The input matrix.
        div (int or float): The number to divide the matrix elements by.

    Returns:
        list of lists of float: The new matrix with elements rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.
    """

    if not all(isinstance(row, list) for row in matrix) or \
            not all(all(isinstance(element, (int, float)) for element in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    return (new_matrix)
