#!/usr/bin/python3

"""
Module that defines the BaseGeometry class.
"""


class BaseGeometry:
    """
    A class representing basic geometry.
    """

    def area(self):
        """
        Raises an Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the given value as an integer.

        Parameters:
        - name: A string representing the name of the value.
        - value: The value to be validated.

        Raises:
        - TypeError if value is not an integer.
        - ValueError if value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
