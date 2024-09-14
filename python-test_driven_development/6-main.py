#!/usr/bin/python3
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
"""Tester for Unittests"""
max_integer = __import__('6-max_integer').max_integer

print(max_integer([1, 2, 3, 4]))
print(max_integer([1, 3, 4, 2]))
