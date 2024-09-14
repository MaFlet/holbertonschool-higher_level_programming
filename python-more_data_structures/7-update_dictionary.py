#!/usr/bin/python3
"""
Script that replaces or adds key/value in a
dictionary
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value


def update_dictionary(a_dictionary, key, value):
    """Function replacing and adding key/value"""
    a_dictionary[key] = value
    return a_dictionary
