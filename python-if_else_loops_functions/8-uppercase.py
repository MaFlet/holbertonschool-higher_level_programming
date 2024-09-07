#!/usr/bin/python3
"""
This script prints a string in uppercase followed by
a new line.
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string


def uppercase(my_string):
    """
    Function that prints uppercase characters.
    """
    result = []
    for letter in my_string:
        if 'a' <= letter <= 'z':
            letter = chr(ord(letter) - 32)
        result.append(letter)
    print("".join(result))
