#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    numerator = 0
    denominator = 0
    for values in my_list:
        numerator += values[0] * values[1]
        denominator += values[1]
    return (numerator / denominator)
