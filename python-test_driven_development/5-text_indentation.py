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

    i = 0
    while i < len(text) and text[i] == ' ':
        i += 1

    while i < len(text):
        print(text[i], end="")
        if text[i] == "\n" or text[i] in ".?:":
            if text[i] in ".?:":
                print("\n")
                i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
