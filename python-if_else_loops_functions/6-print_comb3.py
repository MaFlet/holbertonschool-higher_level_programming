#!/usr/bin/python3
"""
This script prints all possible different combinations
of 2 digits
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
for number in range(0, 10):
    for number2 in range(number + 1, 10):
        if number < 9 or number2 < 9:
            print("{:02d}, ".format(number * 10 + number2), end="")
        else:
            print("{:02d}".format(number * 10 + number2))
