#!/usr/bin/python3
"""Node Class"""


class Node:
    """
    Node class that defines a node of a singly linked list.

    Attributes:
        data: The data stored in the node.
        next_node: Reference to the next node in the linked list.
    """

    def __init__(self, data, next_node=None):
        """"
        Initializing a Node object

        Args:
            data: The data stored in the node.
            next_node: Reference to the next node in the linked list.

        Raises:
            TypeError: If the data is not integer or the next_node isnot None
                or node object
        """
        self.__data = data
        self.__next_node = next_node
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """"
        Getter for the data attributes

        Returns:
            int: The data of the node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """"
        Setter for the data attribute.

        Args:
            value (int): The data to be stored in the linked list

        Return:
            TypeError: If the value is not integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """"
        Getter for the next_node attribute.

        Returns:
            Node: Reference for the next_node in the linked list
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter for teh next_node attributes

        Args:
            value (int): Reference for the next_node in the linked list

        Raises:
            TypeError: If value is not None or a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be an integer")
        else:
            self.__next_node = value


"""Singly Linked List Class"""


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            curr = self.head
            while curr.next_node is not None and value > curr.next_node.data:
                curr = curr.next_node
            new_node.next_node = curr.next_node
            curr.next_node = new_node

    def __str__(self):
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()
