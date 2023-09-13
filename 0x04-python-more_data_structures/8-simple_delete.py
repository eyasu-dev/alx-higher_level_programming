#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if len(a_dictionary) != 0:
        if key is None:
            return (a_dictionary)
        elif key not in a_dictionary:
            return (a_dictionary)
        else:
            del a_dictionary[key]
        return (a_dictionary)
    else:
        return ()
