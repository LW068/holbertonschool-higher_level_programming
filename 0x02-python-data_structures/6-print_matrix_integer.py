#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for item in row:
            print("{:4}".format(item), end="")
        print()
