#!/usr/bin/python3
""" Working with singly linked list in python
    Class Node
    Class SinglyLinkedList
"""


class Node:
    """Class constructor
    of the Node
    """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    """Data attribute getter"""
    @property
    def data(self):
        return self.__data

    """Next_node attr getter"""
    @property
    def next_node(self):
        return self.__next_node

    """Data setter"""
    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError('data must be an integer')
        self.__data = value

    """Next_node setter"""
    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')


class SinglyLinkedList:
    """Class constructor"""

    def __init__(self):
        self.__head = None

    def __str__(self):
        default_val = self.__head
        to_be_printed = ''
        while default_val:
            to_be_printed = to_be_printed + str(default_val.data)
            if default_val.next_node:
                to_be_printed = to_be_printed + '\n'
            default_val = default_val.next_node
        return to_be_printed

    """Add nodes in a sorted format"""
    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value)
        elif value <= self.__head.data:
            self.__head = Node(value, self.__head)
        elif value > self.__head.data:
            val = self.__head
            while val is not None:
                if not val.next_node:
                    val.next_node = Node(value)
                    break
                elif value < val.next_node.data:
                    val.next_node = Node(value, val.next_node)
                    break
                val = val.next_node
