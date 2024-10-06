#!/usr/bin/python3
"""
Script that writes a string to a text file (UTF8)
and returns the number of characters written
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value


def write_file(filename="", text=""):
    """
    Function that write file
    Uses "with" statement to open file
    'w' read mode and utf-8 handle UTF-8 encoded files,
    'w' will create file it doesn't file and if file
    already exist, 'w' mode will overwrite contents
    Two parameters:
    filename: name of file to write(default empty string)
    text: text write to file(defaults to an empty string)
    file.read() read the entire contents of file
    Takes parameter filename with default empty string ""
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
