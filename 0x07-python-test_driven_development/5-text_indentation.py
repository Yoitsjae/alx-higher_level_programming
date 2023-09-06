#!/usr/bin/python3
"""
Module to print text with indentation.
"""

def text_indentation(text):
    """
    Function to print text with 2 new lines after '.', '?', and ':'.

    Args:
        text (str): The input text.

    Returns:
        None

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.replace(".", ".\n\n")
    text = text.replace("?", "?\n\n")
    text = text.replace(":", ":\n\n")

    print("\n".join(line.strip() for line in text.split("\n")))
