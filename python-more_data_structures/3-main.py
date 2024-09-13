#!/usr/bin/python3
"""Tester returning set of common elements in two sets"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
common_elements = __import__('3-common_elements').common_elements

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))
