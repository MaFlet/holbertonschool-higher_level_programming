#!/usr/bin/python3
"""
Script that return True if the object is exactly
an instance of the specified class; otherwise False
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value


def is_same_class(obj, a_class):
    """Returns True if object is exactly an instance
    of the specified class"""
    return isinstance(obj, a_class) and type(obj) is a_class
