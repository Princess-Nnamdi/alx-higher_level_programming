#!/usr/bin/python3
"""Define a MagicClass matching exactly a bytecode provided by Holberton."""

import math


class MagicClass:
    """Replicates the functionality described in the given Python bytecode."""

    def __init__(self, radius=0):
        """
        Initialize the MagicClass instance with a given radius.

        :param radius: The radius of the circle (default is 0).
        :type radius: int or float
        :raises TypeError: If radius is not a number (int or float).
        """
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        :return: The area of the circle.
        :rtype: float
        """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """
        Calculate the circumference of the circle.

        :return: The circumference of the circle.
        :rtype: float
        """
        return (2 * math.pi * self.__radius)
