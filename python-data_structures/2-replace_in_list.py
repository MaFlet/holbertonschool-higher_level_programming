#!/usr/bin/python3
"""
Script that replaces an element of a list at a specific
position
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value


def replace_in_list(my_list, idx, element):
    """Function to replaces an element from a list"""
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
