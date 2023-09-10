#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return ()
    else:
        list_len = len(my_list) - 1
        while list_len > -1:
            print("{:d}".format(my_list[list_len]))
            list_len -= 1
