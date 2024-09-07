#!/usr/bin/python3
"""
This script prints a string in uppercase followed by
a new line.
"""
# pylint: disable=invalid-name


def uppercase(my_string):
    """
    Function that prints uppercase characters.
    """
    new_string = ''
    for i in my_string:
        if 'a' <= i <= 'z':
            new_string += chr(ord(i) - 32)
        else:
            new_string += i
    print(f'{new_string}')
