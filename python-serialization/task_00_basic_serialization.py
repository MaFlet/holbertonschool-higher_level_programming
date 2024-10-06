#!/usr/bin/python3
"""
Script that serialize and deserialize Python
dictionary to JSON file.
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value
import json
def serialize_and_save_to_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
