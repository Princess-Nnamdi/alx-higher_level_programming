#!/usr/bin/python3

"""
Module that defines the is_same_class function.
"""


def is_same_class(obj, a_class):
    """
    Checks if the given object is an instance of the specified class.

    Parameters:
    - obj: The object to check.
    - a_class: The class to compare against.

    Returns:
    - True if the object is an instance of the class, False otherwise.
    """
    return type(obj) is a_class
