#!/usr/bin/env python3
"""
Main script for testing lowercase characters
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
islower = __import__('7-islower').islower

print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))
