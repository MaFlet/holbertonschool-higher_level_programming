#!/usr/bin/python3
"""
Script that prints all integers of a list
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value
def print_list_integer(my_list=[]):
    """Function to print list of all integers"""
    for number in my_list:
        print("{}".format(number))
