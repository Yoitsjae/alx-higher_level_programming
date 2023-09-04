#!/usr/bin/python3
Square = __import__('10-square').Square

my_square = Square(5)
print("Area: {}".format(my_square.area()))

print(my_square)

my_square.width = 10
print("Area: {}".format(my_square.area()))

print(my_square)
