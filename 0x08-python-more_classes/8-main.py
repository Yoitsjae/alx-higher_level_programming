#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(2, 3)

print("Area: {}".format(my_rectangle_1.area()))
print("Area: {}".format(my_rectangle_2.area()))

bigger = Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2)
print("{} is bigger".format(bigger))

bigger = Rectangle.bigger_or_equal(my_rectangle_2, my_rectangle_1)
print("{} is bigger".format(bigger))
