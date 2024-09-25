import abc


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
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        """Defining area method"""
        return 3.14159265358979323846 * self.radius ** 2

    def perimeter(self):
        """Defining perimeter method"""
        return 2 * 3.14159265358979323846 * self.radius


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


def test_circle_negative():
    try:
        circle_negative = Circle(-5)
        assert False, "Expected ValueError for negative radius"
    except ValueError as e:
        assert str(e) == "Radius cannot be negative"
