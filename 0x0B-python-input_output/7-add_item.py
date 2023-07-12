#!/usr/bin/python3

import json
import sys

def load_from_json_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_to_json_file(my_obj, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)

if __name__ == '__main__':
    filename = "add_item.json"
    try:
        my_dict = load_from_json_file(filename)
    except FileNotFoundError:
        my_dict = {}

    argc = len(sys.argv)
    if argc > 1:
        for i in range(1, argc):
            my_dict[str(i)] = sys.argv[i]

    save_to_json_file(my_dict, filename)
