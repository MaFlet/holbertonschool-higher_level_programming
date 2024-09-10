#!/usr/bin/python3
"""
Script retrieves an element from a list
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value


def element_at(my_list, idx):
    """Function to retrieve an element from a list"""
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
