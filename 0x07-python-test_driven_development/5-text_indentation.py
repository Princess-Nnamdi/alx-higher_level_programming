#!/usr/bin/python3
# 5-text_indentation.py
"""
Defines a function that adds 2 new lines after each '.', '?', and ':' characters in the text.
"""


def text_indentation(text):
    """
    Adds 2 new lines after '.', '?', and ':' characters in the text.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuations = ['.', '?', ':']
    result = ""
    for char in text:
        result += char
        if char in punctuations:
            result += "\n\n"

    print(result, end="")
