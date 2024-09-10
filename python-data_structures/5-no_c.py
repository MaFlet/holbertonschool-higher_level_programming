#!/usr/bin/python3
"""
Script that removes all characters c and C from a string
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value


def no_c(my_string):
    """Removes all characters c and C from a string"""
    new_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string
