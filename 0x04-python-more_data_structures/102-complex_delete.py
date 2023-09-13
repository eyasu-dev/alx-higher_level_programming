#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    k_list = list(a_dictionary.keys())
    for i in k_list:
        if value == a_dictionary.get(i):
            del a_dictionary[i]
    return (a_dictionary)
