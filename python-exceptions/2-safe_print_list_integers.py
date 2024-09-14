#!/usr/bin/python3
"""
Script the prints the first x elements of a list and
only integers
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value


def safe_print_list_integers(my_list=[], x=0):
    """Prints only integers of the list"""
    count = 0
    try:
        for i in range(x):
            element = my_list[i]
            if isinstance(element, int):
                print("{:d}".format(element), end="")
                count += 1
    except (ValueError, TypeError):
        pass
    print()
    return count
