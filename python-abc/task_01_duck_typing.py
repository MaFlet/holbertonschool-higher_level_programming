import abc
import math


class Shape(metaclass=abc.ABCMeta):
    """Class Shape with 2 methods"""

    @abc.abstractmethod
    def area(self):
        """Defining area method"""

    def perimeter(self):
        """Defining perimeter method"""


class Circle(Shape):
    """Class Circle in Shape class"""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Defining area method"""
        return math.pi * abs(self.radius) ** 2

    def perimeter(self):
        """Defining perimeter method"""
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """Class Rectangle in Shape class"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Defining area method"""
        return self.width * self.height

    def perimeter(self):
        """Defining perimeter method"""
        return 2 * self.width + 2 * self.height


def shape_info(shape):
    """Defining shape_info function"""
    try:
        area = shape.area()
        perimeter = shape.perimeter()
        print(f"Area: {area}")
        print(f"Perimeter: {perimeter}")
    except AttributeError as e:
        print(f"Error: Shape is missing method: {e}")
