#!/usr/bin/python3
"""
This script prints all numbers from 0 to 98 in
decimal and in hexadecimal
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
for number in range(0, 99):
    print("{} = {}".format(number, hex(number)))
