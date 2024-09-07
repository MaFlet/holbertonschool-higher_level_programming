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
    result = ""
    for letter in my_string:
        character = ord(letter)
        if 97 <= character <= 122:
            character -= 32
        result += chr(character)
    print("{}".format(result))
