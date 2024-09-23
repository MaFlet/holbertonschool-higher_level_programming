#!/usr/bin/python3
"""
Script that returns True if the object is an
instance of a class that inherited (directly or
indirectly) by specified class, otherwise False
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value


def inherits_from(obj, a_class):
    """Returns True if object is an instance
    inherited (directly or indirectly) by specified
    class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
