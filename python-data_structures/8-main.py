#!/usr/bin/python3
"""
Script tester that returns a tuple with the
length of a string and its first character
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))
