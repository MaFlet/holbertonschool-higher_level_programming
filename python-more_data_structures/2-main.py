#!/usr/bin/python3
"""Tester adding all unique integers in a list"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
uniq_add = __import__('2-uniq_add').uniq_add

my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))
