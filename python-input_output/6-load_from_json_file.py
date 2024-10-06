#!/usr/bin/python3
"""
Script that creates an Object from a
"JSON file"
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value
import json


def load_from_json_file(filename):
    """
    Function in Python to read a JSON file and
    convert its contents back into a Python object
    Parameter:
    filename: name of JSON file to read
    json.load(file): reads JSON data from the file and
    converts its back into corresponding Python object
    """
    with open(filename, 'r', encoding='utf-8') as file:
        json.load(file)
