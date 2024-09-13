#!/usr/bin/python3
"""
Script that adds all unique integers in a list
(only once for each integer)
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value


def uniq_add(my_list=[]):
    """Function that adds all unique integers once"""
    if my_list is None:
        my_list = []
    return sum(set(filter(lambda x: isinstance(x, int), my_list)))
