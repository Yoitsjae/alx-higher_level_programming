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

if __name__ == '__main__':
    square_1 = Square(5)
    s_square_1 = square_1.to_json_string()
    print(s_square_1)
    print(type(s_square_1))

    square_2 = Square(10)
    s_square_2 = square_2.to_json_string()
    print(s_square_2)
    print(type(s_square_2))
