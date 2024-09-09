#!/usr/bin/python3
"""
This script prints a string in uppercase followed by
a new line.
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=redefined-builtin

def uppercase(str):
    """ Function that prints uppercase characters."""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
