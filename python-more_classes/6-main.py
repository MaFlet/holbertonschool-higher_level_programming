#!/usr/bin/python3
"""
Tester defining a rectangle's area and perimeter
with evaluation
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
Rectangle = __import__('6-rectangle').Rectangle

my_rectangle_1 = Rectangle(2, 4)
my_rectangle_2 = Rectangle(2, 4)
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_1
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_2
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
