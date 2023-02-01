#!/usr/bin/python3
"""
This is the add_item module
The add_item module adds all arguments
to a Python list, and then save them to a file
"""


load = __import__('6-load_from_json_file').load_from_json_file
rt sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    """functon that"""
    try:
        load_this = load_from_json_file("add_item.json")
    except FileNotFoundError:
        load_this = []
    load_this.extend(sys.argv[1:])
    save_to_json_file(load_this, "add_item.json")
