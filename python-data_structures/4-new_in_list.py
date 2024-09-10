#!/usr/bin/python3
"""
Script that replaces an element in a list at a specific
position without modifying the original list
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value


def new_in_list(my_list, idx, element):
    """
    Replaces an element at a specific position without
    modifying the original list
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = my_list[:]
    new_list[idx] = element
    return new_list
