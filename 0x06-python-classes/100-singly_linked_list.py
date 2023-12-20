#!/usr/bin/python3

"""Define classes for a singly-linked list."""


class Node:
    """This class represents a node within a singly-linked list."""
    def __init__(self, data, next_node=None):
        """Creates a new node optional reference to the next node.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node): Reference to the next node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Accessor and mutator for the data attribute."""
        return (self.__data)

    @data.setter
    def data(self, value):
        """Sets the data attribute after ensuring it is an integer.

        Args:
            value: The data value to be set.
        Raises:
            TypeError: If the provided value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Accessor and mutator for the next_node attribute."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Sets the next_node attribute.

        Args:
            value (Node): The next node to be set.
        Raises:
            TypeError: If the provided value is not a Node object or None.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """This class represents a singly-linked list."""
    def __init__(self):
        """Initializes a new singly-linked list with no nodes."""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new node .

        Args:
            value (Node): The value to be stored in the new node.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Defines the string."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
