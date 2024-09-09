#!/usr/bin/python3
""" Script teste to retrieve element from list"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
