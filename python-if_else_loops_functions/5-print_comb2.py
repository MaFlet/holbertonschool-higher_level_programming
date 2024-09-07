#!/usr/bin/python3
"""
This script that prints numbers from 0 to 99
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
for number in range(0, 100):
    if number == 99:
        print("{}".format(number))
    else:
        print("{:02d}".format(number), end=", ")
