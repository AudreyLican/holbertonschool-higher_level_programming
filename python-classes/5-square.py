#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """Defines square attribute"""

    def __init__(self, size=0):
        """
        Initializing the square
        Args:
            size (int): size of the square
            Default to 0.
        Raises:
            TypeError: if size is not a integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """Public instance method"""
    def area(self):
        """
        Returns:
            The current square size
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Return:
            The current square area
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Args:
            value: size of square
        Raises:
            TypeError: if size is not a integer.
            ValueError: if value is less tan zero.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        print in stdoout the square with character #.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
