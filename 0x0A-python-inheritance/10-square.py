#!/usr/bin/python3

"""
Module that defines the Square class.
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


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance.

        Parameters:
        - width: The width of the rectangle.
        - height: The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
        - The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a formatted string representation of the rectangle.

        Format: "[Rectangle] <width>/<height>"
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """
    A class representing a square, inheriting from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Parameters:
        - size: The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a formatted string representation of the square.

        Format: "[Square] <size>/<size>"
        """
        return "[Square] {}/{}".format(self._Rectangle__width,
                                        self._Rectangle__height)
