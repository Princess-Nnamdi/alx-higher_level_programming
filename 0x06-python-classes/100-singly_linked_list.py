#!/usr/bin/python3
"""Define a class Square."""


class Node:
    """Defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """
        Initialize the Node instance with a given data and next_node.

        :param data: The data for the node.
        :type data: int
        :param next_node: The next node in the linked list (default is None).
        :type next_node: Node or None
        :raises TypeError: If data is not an integer or if next_node is not a Node object.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieve the data of the node.

        :return: The data of the node.
        :rtype: int
        """
        return (self.__data)

    @data.setter
    def data(self, value):
        """
        Set the data of the node.

        :param value: The data for the node.
        :type value: int
        :raises TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieve the next node in the linked list.

        :return: The next node or None if there's no next node.
        :rtype: Node or None
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node in the linked list.

        :param value: The next node or None if there's no next node.
        :type value: Node or None
        :raises TypeError: If value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list."""

    def __init__(self):
        """Initialize the SinglyLinkedList instance with an empty head."""
        self.head = None

    def sorted_insert(self, value):
        """
        Insert a new Node into the correct sorted position in the list (increasing order).

        :param value: The value to be inserted in the list.
        :type value: int
        """
        new_node = Node(value)
        if not self.head or value <= self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node and value > current.next_node.data:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Print the entire list in stdout, one node number by line."""
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return (result.strip())
