#!/usr/bin/python3
"""Script that prints an integer with "{:d}.format()"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value


def safe_print_integer(value):
    """Prints an integer with the format string"""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
