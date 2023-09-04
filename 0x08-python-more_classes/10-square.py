#!/usr/bin/python3
from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)

    def __str__(self):
        return super().__str__()
