#!/usr/bin/python3
"""
This script prints a string in uppercase followed by
a new line.
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string


def uppercase(str):
    """
    Function that prints uppercase characters.
    """
    new_string = ''
    for char in str:
        if 'a' <= char <= 'z':
            new_string += chr(ord(char) - 32)
        else:
            new_string += char
    print("{}".format(new_string))
