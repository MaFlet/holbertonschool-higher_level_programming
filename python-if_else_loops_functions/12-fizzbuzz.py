#!/usr/bin/python3
"""
Script prints the numbers from 1 to 100
separated by a space
"""
# pylint: disable=invalid-name


def fizzbuzz():
    """
    Funtion define as printng fizzbuzz
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")


if __name__ == "__main__":
    fizzbuzz()
    print()
