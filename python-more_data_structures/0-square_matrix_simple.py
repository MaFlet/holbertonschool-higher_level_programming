#!/usr/bin/python3
"""
Script that computes the square value of all integers
of a matrix
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value


def square_matrix_simple(matrix=[]):
    """Printing the sqaure matrix value"""
    if not matrix:
        return []
    result = []
    for row in matrix:
        new_row = []
        for value in row:
            new_row.append(value ** 2)
        result.append(new_row)

    return result
