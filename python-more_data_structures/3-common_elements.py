#!/usr/bin/python3
"""
Script that returns a set of common elements in
two sets
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value


def common_elements(set_1, set_2):
    """Function that adds set of common integers"""
    return list(filter(lambda x: x in set_2, set_1))
