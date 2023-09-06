#!/usr/bin/python3
"""
Module to divide all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """
    Function to divide all elements of a matrix by a number.

    Args:
        matrix (list of lists): The matrix of integers/floats.
        div (int/float): The divisor.

    Returns:
        list of lists: A new matrix with elements divided by div.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If rows of matrix are not of the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is 0.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(matrix[0]) == len(row) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]
    return new_matrix
