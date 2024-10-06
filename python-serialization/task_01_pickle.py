#!/usr/bin/python3
"""
Script that serialize and deserialize Python
objects using the Pickle module
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value
import pickle
import os


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Takes filename as parameter and uses pickle.dump()
        to serialize the instance to the specified file in
        binary mode 'wb'
        """
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """
        Reads object using pickle.load() and returns the
        instance of CustomObject. It opens file in binary
        read mode 'rb'
        """
        if not os.path.isfile(filename):
            print(f"Error: The file '{filename}' does not exist.")
            return None

        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except EOFError:
            print(f"Error: The file '{filename}' is empty or corrupted")
            return None
        except Exception as e:
            print(f"An error occurred while deserializing: {e}")
            return None
