#!/usr/bin/python3
"""
This script prints a string in uppercase followed by
a new line
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string


def uppercase(my_string):
    """
    Function that print uppercase characters
    """
    result = []
    for letter in my_string:
        if ord(letter) >= 97 and ord(letter) <= 122:
            letter = chr(ord(letter) - 32)
        result.append(letter)
    print("{}".format("".join(result)))
