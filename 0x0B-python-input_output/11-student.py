#!/usr/bin/env python3

import json

class Square:
    def __init__(self, size=0):
        self.size = size

    def to_dictionary(self):
        return {
            'size': self.size
        }

    def to_json_string(self):
        return json.dumps(self.to_dictionary())

    def save_to_json_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(self.to_json_string())

if __name__ == '__main__':
    square = Square(5)
    square.save_to_json_file("square.json")
