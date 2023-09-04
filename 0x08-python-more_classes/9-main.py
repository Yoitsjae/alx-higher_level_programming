#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print("Area: {}".format(my_square.area()))

print(my_square)

my_square.width = 10
print("Area: {}".format(my_square.area()))

print(my_square)
