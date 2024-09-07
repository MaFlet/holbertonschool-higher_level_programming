#!/usr/bin/python3
"""
This script prints all numbers from 0 to 98 in
decimal and in hexadecimal
"""
# pylint: disable=invalid-name
for number in range(0, 98):
    print(f"{number} = {hex(number)}", end="")
