#!/usr/bin/python3
"""
Script that adds 2 tuples
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value


def add_tuple(tuple_a=(), tuple_b=()):
    """Adds 2 tuples"""
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
