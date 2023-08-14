#!/usr/bin/python3

"""
Module that defines the MyInt class.
"""


class MyInt(int):
    """
    A class representing a rebellious integer.
    """

    def __init__(self, value):
        """
        Initializes a MyInt instance.

        Parameters:
        - value: The value of the integer.
        """
        self.__value = value

    def __eq__(self, other):
        """
        Inverts the equality operator.
        """
        return self.__value != other

    def __ne__(self, other):
        """
        Inverts the inequality operator.
        """
        return self.__value == other

    def __str__(self):
        """
        Returns a string representation of the integer.
        """
        return str(self.__value)
