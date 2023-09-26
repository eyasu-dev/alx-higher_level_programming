#!/usr/bin/python3
"""
Module 3-square
Define class square
"""


class Square:
    """ Defines the class Square object
    Private instance attribute: size
    """
    def __init__(self, size=0):
        """ initialize the method for square object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ public method that returns
        the current square of the object
        """
        return (self.__size ** 2)
