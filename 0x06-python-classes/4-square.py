#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """define a square."""

    def __init__(self, size=0):
        """Initialize a Square.

        Args:
            size: The size of square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.size = size

    @property
    def size(self):
        """get the size of square"""
        return (self._size)

    @size.setter
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return the are of the square """
        return (self.__size * self.__size)
