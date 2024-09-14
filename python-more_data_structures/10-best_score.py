#!/usr/bin/python3
"""
Script that returns a key with the biggest
integer value
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value


def best_score(a_dictionary):
    """Function returning the biggest value"""
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
