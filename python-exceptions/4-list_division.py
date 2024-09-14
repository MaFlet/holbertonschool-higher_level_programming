#!/usr/bin/python3
"""
Script the divides element by element 2 lists
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value


def list_division(my_list_1, my_list_2, list_length):
    """Dividing elements between 2 lists"""
    list = [0] * list_length
    for i in range(list_length):
        try:
            list[i] = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            pass
    return list
