#!/usr/bin/python3
"""Defines the implementation of singly linked list"""


class Node:
    """Represents a node in a data structure"""

    def __init__(self, data, next_node=None):
        """
        Initialize a Node with the given data and next_node

        Args:
            data (int): The value associated with the node.
            next_node (Node): Address of the next node in the list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Get the value of the node.

        Returns:
            int: The value associated with the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the value of the node.

        Args:
            value (int): The new value to be set for the node.

        Raises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Get the next node.

        Returns:
            Node: The next node in the list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node.

        Args:
            value (Node): The new node to be set as the next node.

        Raises:
            TypeError: If the value is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A class that represents a singly linked list."""

    def __init__(self):
        """Initialize an empty singly linked list."""
        self.__head = None

    def sorted_insert(self, value) -> None:
        """
        Inserts a new Node into the correct sorted position
            in the list (in increasing order).

        Args:
            value (int): The value to be inserted.
        """
        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node
        elif value <= self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while (current.next_node is not None
                   and
                   value > current.next_node.data):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self) -> str:
        """
        Return a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.
        """
        result = ""
        current = self.__head
        while current is not None:
            result += str(current.data) + '\n'
            current = current.next_node

        return result.rstrip('\n')
