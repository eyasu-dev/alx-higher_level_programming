#!/usr/bin/python3
"""
Module 5-square
Define class Square
"""


class Square:
    """ Defines a Class Square object.
    Private instance attribute: size.
    Private instance attribute: position
    """

    def __init__(self, size=0, position=(0, 0)):
        """ intializes the method square object
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ Method that returns the current position
        of the object square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Method to set the size
        value of the object square
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ Method that returns the area
        of the object square
        """
        return (self.__size ** 2)

    def my_print(self):
        """ Method to print '#'
        of the object square to the stdout
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(0, self.size):
                for j in range(self.position[0]):
                    print(" ", end='')
                for k in range(self.size):
                    print('#', end="")
                print()
