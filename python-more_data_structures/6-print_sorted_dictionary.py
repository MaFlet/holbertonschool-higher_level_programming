#!/usr/bin/python3
"""
Script that prints a dictionary by ordered keys
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value


def print_sorted_dictionary(a_dictionary):
    """Function printing dictionary by ordered keys"""
    for key in sorted(a_dictionary, key=lambda x: x):
        print(f"{key}: {a_dictionary[key]}")
