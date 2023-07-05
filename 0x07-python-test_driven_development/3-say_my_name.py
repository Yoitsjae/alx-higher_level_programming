#!/usr/bin/env python3

"""
Say My Name Module

This module contains a function to print a person's name.

"""

def say_my_name(first_name, last_name=""):
    """
    Print the person's name.

    Args:
        first_name (str): The first name of the person.
        last_name (str): The last name of the person (default is empty string).

    Raises:
        TypeError: If `first_name` is not a string or `last_name` is not a string.

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
