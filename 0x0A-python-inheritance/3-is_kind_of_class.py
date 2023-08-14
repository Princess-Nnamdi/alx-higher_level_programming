#!/usr/bin/python3

"""
Module that defines the is_kind_of_class function.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the given object is an instance of,
    or a subclass of, the specified class.

    Parameters:
    - obj: The object to check.
    - a_class: The class to compare against.

    Returns:
    - True if the object is an instance of or
    subclass of the class, False otherwise.
    """
    return isinstance(obj, a_class)
