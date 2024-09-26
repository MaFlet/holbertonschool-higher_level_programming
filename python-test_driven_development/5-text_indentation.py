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
    i = 0
    text_length = len(text)

    while i < text_length:
        result += text[i]

        if text[i] in {'.', '?', ':'}:
            result += "\n\n"
            while i + 1 < text_length and text[i + 1] == ' ':
                i += 1

        i += 1
    print(result.strip())
