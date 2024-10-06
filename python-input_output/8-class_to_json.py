#!/usr/bin/python3
"""
Script that returns the dictionary with simple data
structure for JSON serialization of an object
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value


def class_to_json(obj):
    """
    Return a dictionary representation of an object
    for JSON serialization
    Parameter:
    obj: expected to be an instance of class
    obj.__dict__.items() iterates over the attributes
    """
    if not hasattr(obj, "__dict__"):
        return {}

    obj_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            obj_dict[key] = value

    return obj_dict
