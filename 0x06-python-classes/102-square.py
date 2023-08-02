#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """
        Initialize the Square instance with a given size.

        :param size: The size of the square (default is 0).
        :type size: float or int
        :raises TypeError: If size is not a number (float or integer).
        :raises ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieve the size of the square.

        :return: The size of the square.
        :rtype: float or int
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        :param value: The size of the square.
        :type value: float or int
        :raises TypeError: If value is not a number (float or integer).
        :raises ValueError: If value is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        :return: The area of the square.
        :rtype: float or int
        """
        return (self.__size ** 2)

    def __eq__(self, other):
        """Check if two squares have equal areas."""
        return (self.area() == other.area())

    def __ne__(self, other):
        """Check if two squares have different areas."""
        return (self.area() != other.area())

    def __lt__(self, other):
        """Check if the area of the current square 
        is less than the area of another square."""
        return (self.area() < other.area())

    def __le__(self, other):
        """Check if the area of the current square is less than 
        or equal to the area of another square."""
        return (self.area() <= other.area())

    def __gt__(self, other):
        """Check if the area of the current square is 
        greater than the area of another square."""
        return (self.area() > other.area())

    def __ge__(self, other):
        """Check if the area of the current square is greater than 
        or equal to the area of another square."""
        return (self.area() >= other.area())
