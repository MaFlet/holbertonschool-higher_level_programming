#!/usr/bin/python3
"""Tester that define a square"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)
