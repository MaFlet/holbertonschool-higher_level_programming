#!/usr/bin/python3
"""
Tester when Square clas inherits from
Rectangle with size attribute
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value
Square = __import__('11-square').Square

s = Square(13)

print(s)
print(s.area())
