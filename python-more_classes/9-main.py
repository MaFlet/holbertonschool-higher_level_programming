#!/usr/bin/python3
"""
Tester defining a rectangle's area and perimeter
with evaluation
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)
