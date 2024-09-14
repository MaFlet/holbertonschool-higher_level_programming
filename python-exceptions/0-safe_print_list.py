#!/usr/bin/python3
"""Script that prints x elements of a list"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value


def safe_print_list(my_list=[], x=0):
    """Prints elements on list"""
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass
    print()
    return count
