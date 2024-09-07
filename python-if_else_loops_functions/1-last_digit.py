#!/usr/bin/python3
"""
The script assign a random signed number to the variable number
each time it is executed
"""
# pylint: disable=invalid-name
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if number < 0:
    last_digit = -last_digit
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit < 6 and last_digit != 0:
    print(f"Last digit of {number} is {last_digit} "
           "and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {last_digit} and is 0")
last_digit = random.randint(0, 9)
