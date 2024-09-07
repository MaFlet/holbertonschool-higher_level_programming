#!/usr/bin/python3
"""
This script prints ASCII alphabet, in lowercase except
q and e, not followed by a new line
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
for i in range(97, 123):
    if i not in (101, 113):
        print("{}".format(chr(i)), end="")
        