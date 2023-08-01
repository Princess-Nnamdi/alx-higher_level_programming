#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Defines a Square."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the Square instance with a given size and position.

        :param size: The size of the square (default is 0).
        :type size: int
        :param position: The position of the square (default is (0, 0)).
        :type position: tuple of 2 positive integers
        :raises TypeError: If size is not an integer or if position is not a tuple of 2 positive integers.
        :raises ValueError: If size is less than 0 or if position contains non-positive integers.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Retrieve the position of the square.

        :return: The position of the square.
        :rtype: tuple
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        :param value: The position of the square.
        :type value: tuple of 2 positive integers
        :raises TypeError: If value is not a tuple of 2 positive integers.
        :raises ValueError: If value contains non-positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = value
        if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

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

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0], "#" * self.__size)
