#!/usr/bin/python3
"""
Tester when Rectangle class inherits from
BaseGeometry function having width and height
attributes
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value
Rectangle = __import__('9-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(r.area())
