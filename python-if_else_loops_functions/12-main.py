#!/usr/bin/env python3
"""
This script will import function from file
12-fizzbuzz.py
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
fizzbuzz = __import__('12-fizzbuzz').fizzbuzz

fizzbuzz()
print("")
