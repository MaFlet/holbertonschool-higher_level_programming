#!/usr/bin/python3
"""
Script tester for calculating 2 integers with
different functions
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} + {} = {}".format(a, b, sub(a, b)))
    print("{} + {} = {}".format(a, b, mul(a, b)))
    print("{} + {} = {}".format(a, b, div(a, b)))
