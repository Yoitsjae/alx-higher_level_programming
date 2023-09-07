#!/usr/bin/python3
"""
Module to add two integers.
"""

def add_integer(a, b=98):
    """
    Function to add two integers.

    Args:
        a (int): The first integer.
        b (int, optional): The second integer. Defaults to 98.

    Returns:
        int: The addition of a and b.
    
    Raises:
        TypeError: If a or b is not an integer or float.
    """

   if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
