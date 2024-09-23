#!/usr/bin/python3
"""
Script that returns True if the object is an instance
of, or if the object is an instance of a class the
inherited by the specified class, otherwise False
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value


def is_kind_of_class(obj, a_class):
    """Returns True if object is an instance of
    or inherited by specified class"""
    return isinstance(obj, a_class)
