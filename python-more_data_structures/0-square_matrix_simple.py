#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []

    for i in matrix:
        #calculate square of each element
        square = list(map(lambda nb: nb ** 2, i))
        #add/append square of each element of matrix
        new_matrix.append(square)
    return new_matrix
