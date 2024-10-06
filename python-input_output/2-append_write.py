#!/usr/bin/python3
"""
Script that appends a string at the end of a
text file (UTF8) and returns the number of characters
added
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value


def append_write(filename="", text=""):
    """
    Function that write file
    Uses "with" statement to open file
    'w' read mode and utf-8 handle UTF-8 encoded files,
    'w' will create file it doesn't file and if file
    already exist, 'w' mode will overwrite contents
    Two parameters:
    filename: name of file to append(default empty string)
    text: text append to file(defaults to an empty string)
    file.write(text) appends specified text at the end of
    file
    Return: number of characters using len(text)
    """
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
    return len(text)
