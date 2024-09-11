#!/usr/bin/python3
"""
Script that switch value of a and b
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value
a = 89
b = 10
a, b = b, a
print("a={:d} - b={:d}".format(a, b))
