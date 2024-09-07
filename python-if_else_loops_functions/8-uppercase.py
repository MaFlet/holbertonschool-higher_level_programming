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
    new_string = ''
    for i in my_string:
        if ord(i) >= 97 and ord(i) < 123:
            new_string = new_string + chr(ord(i) - 32)
        else:
            new_string = new_string + i
    print('{}'.format(new_string))
