#!/usr/bin/python3
"""
Script that finds all multiples of 2 in a list
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value


def divisible_by_2(my_list=[]):
    """Search all multiples of 2"""
    return [value % 2 == 0 for value in my_list]
