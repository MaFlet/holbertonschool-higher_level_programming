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
    print('{}'.format(''.join(chr(ord(i) - 32)
                              if 'a' <= i <= 'z' else i for i in my_string)))
