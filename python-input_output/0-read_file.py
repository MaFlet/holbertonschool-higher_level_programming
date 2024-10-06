#!/usr/bin/python3
"""
Script that reads a text file (UTF8) and prints
it to stdout
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value


def read_file(filename=""):
    """
    Function that read file
    Uses "with" statement to open file
    'r' read mode and utf-8 handle UTF-8 encoded files
    file.read() read the entire contents of file
    Takes parameter filename with default empty string ""
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')
