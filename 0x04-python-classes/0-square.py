#!/usr/bin/python3
"""This module contains a class representing a simple square.
Example:
    >>>new_square = square(2)
"""


class Square:
    """Class representing a simple square
    """
    def __init__(self, _size):
        """Initialize a simple Square
        Args:
            _size (int): Size of the Square.
        """
        self.__size = _size
