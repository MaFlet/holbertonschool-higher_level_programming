#!/usr/bin/python3
"""
Script tester for printing addition results
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
if __name__ == "__main__":
    from add_0 import add

    a = 1
    b = 2

    print("{} + {} = {}".format(a, b, add(a, b)))
