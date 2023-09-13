#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return
    else:
        new_matrix = []
        for i in matrix:
            sq_list = [x ** 2 for x in i]
            new_matrix.append(sq_list)
        return (new_matrix)
