#!/usr/bin/python3
def matrix_divided(matrix, div):
    new_matrix = [] 
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        new_row = []
        for s in row:
            if type(s) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_row.append(int(s / div))
        new_matrix.append(new_row)
    return new_matrix
