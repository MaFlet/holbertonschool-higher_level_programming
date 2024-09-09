#!/usr/bin/python3
"""
Script tester that finds the biggest integer
of a list
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
