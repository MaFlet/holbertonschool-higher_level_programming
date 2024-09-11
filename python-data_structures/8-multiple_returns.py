#!/usr/bin/python3
"""
Script that returns a tuple with the length of a string
and its first character
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value


def multiple_returns(sentence):
    """Length of string and its first character"""
    if not sentence:
        return None
    return (len(sentence), sentence[0])
