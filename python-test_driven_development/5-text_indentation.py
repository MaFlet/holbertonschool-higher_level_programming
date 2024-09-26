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
    punctuation = ['.', '?', ':']
    current_line = ""

    for char in text:
        current_line += char
        if char in punctuation:
            print(current_line.strip())
            print()

    if current_line:
        print(current_line.strip())
