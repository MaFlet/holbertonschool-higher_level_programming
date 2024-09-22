#!/usr/bin/python3
"""
Script that prints a text with 2 new lines after each
of these characters: ., ? and :
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value


def text_indentation(text):
    """Print 2 new lines in text"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    for char in text:
        result += char
        if char in ('.', '?', ':'):
            result += '\n\n'
    for line in result.splitlines():
        print(line.strip())
