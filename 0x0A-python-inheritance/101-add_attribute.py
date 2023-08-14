#!/usr/bin/python3

"""
Module that defines the add_attribute function.
"""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if possible.

    Parameters:
    - obj: The object to which the attribute should be added.
    - name: The name of the attribute.
    - value: The value of the attribute.

    Raises:
    - TypeError if the object can't have a new attribute.
    """
    if hasattr(obj, "__dict__") or hasattr(obj, "__slots__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
