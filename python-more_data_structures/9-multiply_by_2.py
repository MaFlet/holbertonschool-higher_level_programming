#!/usr/bin/python3
"""
Script that returns a new dictionary with all
values multiplied by 2
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value


def multiply_by_2(a_dictionary):
    """Function mutiplying values by 2"""
    return {key: value * 2 for key, value in a_dictionary.items()}
