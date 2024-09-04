#!/usr/bin/python3
"""
This script print 3 times a string stored in variable str,
followed by its first 9 characters
"""
# pylint: disable=invalid-name
my_string = "Holberton School"
print(my_string * 3 + my_string[:9])
