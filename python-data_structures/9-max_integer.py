#!/usr/bin/python3
"""
Script that finds the biggest integer of a list
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value


def max_integer(my_list=[]):
    """Search biggest integer of list"""
    if not my_list:
        return None
    biggest = my_list[0]
    for value in my_list:
        if value > biggest:
            biggest = value
    return biggest
