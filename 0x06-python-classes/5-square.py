#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Defines a Square."""

    def __init__(self, size=0):
        """
        Initialize the Square instance with a given size.

        :param size: The size of the square (default is 0).
        :type size: int
        :raises TypeError: If size is not an integer.
        :raises ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieve the size of the square.

        :return: The size of the square.
        :rtype: int
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        :param value: The size of the square.
        :type value: int
        :raises TypeError: If value is not an integer.
        :raises ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        :return: The area of the square.
        :rtype: int
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        Print the square with the character '#'.

        If size is equal to 0, print an empty line.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)
