#!/usr/bin/python3
"""
Define class Square
"""


class Square:
    """ Defines a Class Square object.
    Private instance attribute: size.
    Private instance attribute: position
    Getters and setters implemented
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
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
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
        if self.__size != 0:
            if self.position[1] is not 0:
                print('\n' * self.position[1], end="")
            for x in range(self.size):
                print(' ' * self.position[0], end="")
                print('#' * self.size)
        else:
            print()

    def __str__(self):
        printed = ''
        if self.size != 0:
            if self.position[1] is not 0:
                printed += '\n' * self.position[1]
            for x in range(self.size):
                printed += ' ' * self.position[0]
                printed += '#' * self.size
                if x != self.__size - 1:
                    printed += '\n'
        else:
            printed += ''
        return printed
