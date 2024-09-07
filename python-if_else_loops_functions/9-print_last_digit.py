#!/usr/bin/python3
"""
This script prints the last digit of the number
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string


def print_last_digit(number):
    """
    Function define as printing the last digit
    of the number
    """
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit
