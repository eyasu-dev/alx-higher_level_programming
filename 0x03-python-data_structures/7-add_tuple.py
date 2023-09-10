#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_total = ()
    if (len(tuple_a)) == 0 and len(tuple_b) == 0:
        tuple_total = (0, 0)
        return tuple_total
    elif (len(tuple_b)) == 1 and len(tuple_a) == 1:
        tuple_total = ((tuple_a[0]) + (tuple_b[0]), 0)
        return tuple_total
    if (len(tuple_a)) == 0 and len(tuple_b) == 2:
        tuple_total = ((tuple_b[0]), (tuple_b[1]))
        return tuple_total
    elif (len(tuple_b)) == 0 and len(tuple_a) == 2:
        tuple_total = ((tuple_a[0]), (tuple_a[1]))
        return tuple_total
    if (len(tuple_a)) < 2 and len(tuple_b) == 2:
        tuple_total = ((tuple_a[0] + tuple_b[0]), (tuple_b[1] + 0))
        return tuple_total
    elif (len(tuple_b)) < 2 and len(tuple_a) == 2:
        tuple_total = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + 0))
        return tuple_total
    if (len(tuple_a)) == 0 and len(tuple_b) == 2:
        tuple_total = ((tuple_b[0]), (tuple_b[1]))
        return tuple_total
    elif (len(tuple_b)) == 0 and len(tuple_a) == 2:
        tuple_total = ((tuple_a[0]), (tuple_a[1]))
        return tuple_total
    if (len(tuple_a)) > 2 or (len(tuple_b)) > 2:
        tuple_total = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))
        return tuple_total
    elif (len(tuple_a)) == 2 or (len(tuple_b)) == 2:
        tuple_total = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))
        return tuple_total
