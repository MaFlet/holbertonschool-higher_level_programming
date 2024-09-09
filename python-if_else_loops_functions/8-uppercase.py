#!/usr/bin/python3
"""
This script prints a string in uppercase followed by
a new line.
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=redefined-builtin

def uppercase(str):
    """
    Function that prints uppercase characters.
    """
    for char in str:
        if 'a' <= char <= 'z':
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print()
