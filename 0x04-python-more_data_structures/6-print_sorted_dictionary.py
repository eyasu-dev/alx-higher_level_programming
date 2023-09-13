#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if len(a_dictionary) != 0:
        sort_list = sorted(a_dictionary.keys())
        for i in sort_list:
            print(f"{i}: {a_dictionary[i]}")
