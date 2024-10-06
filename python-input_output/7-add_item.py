#!/usr/bin/python3
"""
Script that adds all arguments to a Python list
then save them to a file
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    filename = "add_item.json"
    my_list = []

    try:
        my_list = load_from_json_file(filename)
    except FileNotFoundError:
        pass
    my_list.extend(sys.argv[1:])
    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    main()
