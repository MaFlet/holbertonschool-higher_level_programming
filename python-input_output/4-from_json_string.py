#!/usr/bin/python3
"""
Script that returns an object (Python data strcture)
represented by a JSON string
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value
import json


def from_json_string(my_str):
    """
    Function that convert python objects to
    JSON format
    Parameter:
    my_str: object to convert to JSON string
    json.loads(my_str): parses JSON string and
    converts into corresponeing Python object
    """
    return json.loads(my_str)
