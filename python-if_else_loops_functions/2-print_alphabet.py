#!/usr/bin/python3
"""
This script prints ASCII alphabet, in lowercase
not followed by a new line.
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
for i in range(97, 123):
    print("{}".format(chr(i)), end="")
