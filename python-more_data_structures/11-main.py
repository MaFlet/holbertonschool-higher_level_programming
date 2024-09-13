#!/usr/bin/python3
"""
Tester returning list with all values multiplied by a
number without using any loops
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
multiply_list_map = __import__('11-multiply_list_map').multiply_list_map

my_list = [1, 2, 3, 4, 6]
new_list = multiply_list_map(my_list, 4)
print(new_list)
print(my_list)
