#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if len(a_dictionary) == 0:
        return ()
    else:
        new_dict = {}
        for i in a_dictionary:
            new_dict[i] = (a_dictionary[i] * 2)
    return new_dict
