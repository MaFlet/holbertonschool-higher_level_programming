#!/usr/bin/python3
"""
This script checks for lowercase character
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string


def islower(c):
    """
    Function that checks characters if they are
    lowercase
    """
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
