#!/usr/bin/python3
"""
Script that returns the JSON representation
of an object(string)
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value
import json


def to_json_string(my_obj):
    """
    Function that convert python objects to
    JSON format
    Parameter:
    my_obj: object to convert to JSON string
    json.dumps(my_obj) converts object into its
    JSON string representation
    """
    return json.dumps(my_obj)
