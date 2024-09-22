#!/usr/bin/python3
"""Tester define an empty class for defining rectangle"""
# pylint: disable=invalid-name
Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)
