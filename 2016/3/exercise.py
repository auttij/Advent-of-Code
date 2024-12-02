import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init


def transpose(matrix):
    rows = len(matrix)
    column = len(matrix[0])
    result = [[0 for i in range(rows)] for j in range(column)]

    for r in range(rows):
        for c in range(column):
            # here we are grabbing the row data of matrix and putting it in the column on the result
            result[c][r] = matrix[r][c]
    return result


def count_triangles(arr):
    possible = 0
    for a, b, c in arr:
        if a + b > c and a + c > b and b + c > a:
            possible += 1
    return possible


@timer
@print_result
def exercise1(arr):
    return count_triangles(arr)


@timer
@print_result
def exercise2(arr):
    new_arr = []
    for i in range(0, len(arr), 3):
        m = arr[i : i + 3]
        new_arr += transpose(m)
    return count_triangles(new_arr)


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_int_tuple_arr, args)
    exercise1(arr.copy())
    exercise2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
