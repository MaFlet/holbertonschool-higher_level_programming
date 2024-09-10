#!/usr/bin/python3
"""
Script that prints a matrix of integers
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value


def print_matrix_integer(matrix=[[]]):
    """Prints matrix of integers"""
    for row in matrix:
        print(" ".join("{:d}".format(element) for element in row))
