#!/usr/bin/python3

class Rectangle:
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = str(self.print_symbol) * self.__width + "\n"
        return (rectangle * (self.__height - 1)) + str(self.print_symbol) * self.__width

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rectangle_1, rectangle_2):
        if not isinstance(rectangle_1, Rectangle):
            raise TypeError("rectangle_1 must be an instance of Rectangle")
        if not isinstance(rectangle_2, Rectangle):
            raise TypeError("rectangle_2 must be an instance of Rectangle")
        
        area_1 = rectangle_1.area()
        area_2 = rectangle_2.area()
        
        if area_1 >= area_2:
            return rectangle_1
        else:
            return rectangle_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
