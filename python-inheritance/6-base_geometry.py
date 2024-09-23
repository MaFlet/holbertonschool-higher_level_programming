#!/usr/bin/python3
"""
Script that write an empty class BaseGeometry
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value


class BaseGeometry:
    """Class for BaseGeometry"""
    def area(self):
        raise Exception("area() is not implemented")
