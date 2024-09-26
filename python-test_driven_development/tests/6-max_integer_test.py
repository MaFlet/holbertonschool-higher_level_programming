#!/usr/bin/python3
"""Unittest for max_integer"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def text_regular_case(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([10, 5, 7]), 10)

    def test_with_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([-1, 2, 3]), 3)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 5, 3, 4]), 5)
        self.assertEqual(max_integer([1, 2, 8, 4, 5]), 8)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_single_element_list(self):
        self.assertEqual(max_integer([42]), 42)

    def test_floats_and_integers(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3]), 3.3)
        self.assertEqual(max_integer([1, 2.5, 3]), 3)

    def test_duplicates(self):
        self.assertEqual(max_integer([1, 1, 1]), 1)
        self.assertEqual(max_integer([3, 3, 3, 3, 3]), 3)

if __name__ == "__main__":
    unittest.main()
