import abc


class Animal(metaclass=abc.ABCMeta):
    """Class Animal"""

    @abc.abstractmethod
    def sound(self):
        """Defining sound method"""


class Dog(Animal):
    """Class dog in Animal class"""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """Class cat in Animal class"""
    def sound(self):
        return "Meow"
