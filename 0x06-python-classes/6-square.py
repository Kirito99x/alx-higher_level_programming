#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """define a square."""

    def __init__(self, size=0):
        """Initialize a Square.

        Args:
            size: The size of square.
        """
        self.size = size
        @property
        def size(self):
            """get the size of square"""
            return (self._size)
        @size.setter
        def size(self, value):
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        
        @property
        def position(self):
            """get the position of the square"""
            return (self._position)
        
        @position.setter
        def position(self, value):
            if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
                raise TypeError("position must be a tuple of 2 positive integers")
            self.__position = value
            
        def area(self):
            """return the are of the square """
            return (self.__size * self.__size)
        
        def my_print(self):
            """print the square with #"""
            for i in range(0, self.__size):
                [print("#", end="") for j in range(self.__size)]
                print("")
            if self.__ == 0:
                print("")
