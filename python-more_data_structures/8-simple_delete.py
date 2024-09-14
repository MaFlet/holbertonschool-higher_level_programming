#!/usr/bin/python3
"""
Script that deletes a key in a dictionary
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value


def simple_delete(a_dictionary, key=""):
    """Function deleting a key"""
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
