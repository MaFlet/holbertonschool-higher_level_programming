#!/usr/bin/python3
"""
Script that raises a name exception with a
message
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value


def raise_exception_msg(message=""):
    """Raises name exeception with message"""
    raise NameError(message)