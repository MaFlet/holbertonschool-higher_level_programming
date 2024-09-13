#!/usr/bin/python3
"""
Script that returns a set of all elements present
in only one set
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value


def only_diff_elements(set_1, set_2):
    """Function that set all different elements"""
    return set_1 ^ set_2
