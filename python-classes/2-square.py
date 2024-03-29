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
        """
        if not isinstance(size, int):
            raise Exception("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
