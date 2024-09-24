#!/usr/bin/python3
"""
Script that write the class square inherited
in Rectangle
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Class for square that is inherited
    in Rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
