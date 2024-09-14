#!/usr/bin/python3
"""
Script the divides 2 integers and prints the result
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value


def safe_print_division(a, b):
    """Dividing 2 integers and print result"""
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
