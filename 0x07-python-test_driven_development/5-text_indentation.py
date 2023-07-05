#!/usr/bin/python3

"""
This module contains a function that prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each occurrence of ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = [".", "?", ":"]

    for char in chars:
        text = text.replace(char, f"{char}\n\n")

    lines = text.splitlines()
    for line in lines:
        print(line.strip())
