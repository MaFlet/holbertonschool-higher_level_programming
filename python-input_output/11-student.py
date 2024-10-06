#!/usr/bin/python3
"""
Script that writes class Student that defines a
student
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value


class Student:
    """
    Represent a student with 3 public attributes
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns dictionary representation of instance, with
        attributes to be serialized into JSON format
        """
        if attrs is None:
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }
        return {key: getattr(self, key) for key in attrs if hasattr(self, key)}

    def reload_from_json(self, json):
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
