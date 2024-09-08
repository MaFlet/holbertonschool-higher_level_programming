#!/usr/bin/python3
"""
This script prints ASCII alphabet, in lowercase
not followed by a new line.
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
for i in range(122, 96, -1):
    print("{}".format(chr(i) if i % 2 == 0 else chr(i - 32)), end="")
