#!/usr/bin/python3
"""Script that adds 2 integers"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value


def add_integer(a, b=98):
    """Adding 2 integers"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if a > 1e308 or b > 1e308:
        raise OverflowError("number too large")
    a = int(a)
    b = int(b)
    return a + b
