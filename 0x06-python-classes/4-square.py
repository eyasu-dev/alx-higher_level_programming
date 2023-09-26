#!/usr/bin/python3
"""
Module 4-square
Define class Square
"""


class Square:
    """ Defines a Class Square object.
    Private instance attribute: size.
    """

    def __init__(self, size=0):
        """ intializes the method square object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Method that returns the area
        of the object square
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """ Method that returns the current area
        of the object square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Method to set the size
        value of the object square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
