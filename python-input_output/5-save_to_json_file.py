#!/usr/bin/python3
"""
Script that writes an Object to a text file, using
a JSON representation
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value
import json


def save_to_json_file(my_obj, filename):
    """
    Function that write Python Object to a text
    file in JSON format
    Parameter:
    my_obj: object to be serialized
    filename: name of file to write to
    json.dump(my_obj, file): function serializes the
    object and writes it directly to the file
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
