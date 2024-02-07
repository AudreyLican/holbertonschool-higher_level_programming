#!/usr/bin/python3
"""Define a square class"""


class Square:
    """Define square attribute"""

    def __init__(self, size=0):
        """
        Initializing the square.
        Arg:
            size (int): the size of the square
            default to 0.

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
