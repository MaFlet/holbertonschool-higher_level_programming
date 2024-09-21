#!/usr/bin/python3
"""
Tester defining a rectangle's area and perimeter
with evaluation
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
Rectangle = __import__('5-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

del my_rectangle

try:
    print(my_rectangle)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
