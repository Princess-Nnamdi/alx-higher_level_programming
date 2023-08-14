#!/usr/bin/python3

"""
Module that defines the MyList class.
"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list.
    """

    def print_sorted(self):
        """
        Prints the list elements in sorted order.

        The original list order is maintained.

        Example:
        - Input: [3, 1, 2]
        - Output: [1, 2, 3]
        """
        sorted_list = sorted(self)
        print(sorted_list)
