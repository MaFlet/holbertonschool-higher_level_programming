#!/usr/bin/python3
"""
Script that replaces all occurrences of an element
by another in a new list
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value


def search_replace(my_list, search, replace):
    """Function that replace search to replace"""
    new_list = []
    for i in my_list:
        if i == search:
            new_list.append(replace)
        else:
            new_list.append(i)
    return new_list
