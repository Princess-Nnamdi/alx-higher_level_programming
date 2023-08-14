#!/usr/bin/python3

"""
Module that defines the inherits_from function.
"""


def inherits_from(obj, a_class):
    """
    Checks if the given object is an instance of a class
    that inherited from the specified class.

    Parameters:
    - obj: The object to check.
    - a_class: The class to compare against.

    Returns:
    - True if the object is an instance of a class
    that inherited from the class, False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
