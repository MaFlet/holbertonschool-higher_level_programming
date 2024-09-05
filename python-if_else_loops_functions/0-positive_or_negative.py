#!/usr/bin/python3
"""
The script assign a random signed number to the variable number
each time it is executed
"""
# pylint: disable=invalid-name
import random
number = random.randint(-10, 10)
while number != 10:
    if number > 0:
        print(number, "is positive")
    elif number == 0:
        print(number, "is zero")
    else:
        print(number, "is negative")
    number = random.randint(-10, 10)
