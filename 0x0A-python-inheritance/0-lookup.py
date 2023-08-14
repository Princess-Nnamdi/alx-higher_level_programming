#!/usr/bin/python3

"""
Module that defines the lookup function.
"""

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Parameters:
    - obj: The object to inspect.

    Returns:
    - List of attribute and method names.
    """
    return dir(obj)
