#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return ()
    else:
        new_list = []
        for i in my_list:
            if i not in new_list:
                new_list.append(i)
        sum_of_val = 0
        for x in new_list:
            sum_of_val += x
        return (sum_of_val)
