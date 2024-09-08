#!/usr/bin/python3
"""
This script prints the result of the additon of all
arguments
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
import sys

if __name__ == "__main__":
    total = 0
    for arg in sys.argv[1:]:  # Used to get the command-line arguments
        total += int(arg)  # Each argument is cast to an integer
    print(total)  # All values are summed in the total variable
