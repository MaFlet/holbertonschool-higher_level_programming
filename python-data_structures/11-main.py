#!/usr/bin/python3
"""
Script tester that deletes the item at a specific
position in a list
"""
# pylint: disable=invalid-name
delete_at = __import__('11-delete_at').delete_at

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)
