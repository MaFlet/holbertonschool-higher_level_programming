#!/usr/bin/python3
"""
Script to write class MyList that inherits
from list
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value

class MyList(list):
    """List class inherits from list"""


    def print_sorted(self):
        """Sort list in ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)