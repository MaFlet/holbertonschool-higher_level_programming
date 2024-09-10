#!/usr/bin/python3
"""
Script that prints all integers of a list, in
reverse order
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value


def print_reversed_list_integer(my_list=[]):
    """Prints all integers in reverse order"""
    if my_list:
        for number in range(len(my_list) - 1, - 1, - 1):
            print("{:d}".format(my_list[number]))
