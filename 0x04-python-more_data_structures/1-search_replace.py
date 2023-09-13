#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    count = 0
    if my_list is None:
        return ()
    else:
        for i in new_list:
            if i == search:
                new_list[count] = replace
            count += 1
    return new_list
