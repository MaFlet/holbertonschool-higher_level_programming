#!/usr/bin/python3
"""
Tester defining a rectangle's area and perimeter
with string representation
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
Rectangle = __import__('3-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print(str(my_rectangle))
print(repr(my_rectangle))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle)
print(repr(my_rectangle))
