#!/usr/bin/python3
"""
Script that deletes the item at a specific position
in a list
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value


def delete_at(my_list=[], idx=0):
    """deletes an item in a list"""
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
