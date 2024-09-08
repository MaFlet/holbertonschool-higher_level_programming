#!/usr/bin/python3
"""
This script calculate a to the power of b
"""
# pylint: disable=invalid-name


def pow(a, b):
    """
    Function define as computing a to the power
    of b
    """
    result = 1
    for _ in range(abs(b)):
        result *= a
    if b < 0:
        result = 1 / result
    return result
