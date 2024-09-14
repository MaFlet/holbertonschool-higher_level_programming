#!/usr/bin/python3
"""
Script the divides element by element 2 lists
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value


def list_division(my_list_1, my_list_2, list_length):
    """Dividing elements between 2 lists"""
    new_list = []
    for i in range(list_length):
        try:
            num1 = my_list_1[i]
            num2 = my_list_2[i]
            if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
                print("wrong type")
                new_list.append(0)
            else:
                new_list.append(num1 / num2)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        finally:
            pass
        return new_list
