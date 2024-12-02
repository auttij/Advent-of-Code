import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init


@timer
@print_result
def exercise1(arr):
    val = 20151125

    mul = 252533
    mod = 33554393

    def order(row, col):
        diagonal = row + col
        total_in_previous = (diagonal * (diagonal + 1)) // 2
        position_in_diagonal = col
        return total_in_previous + position_in_diagonal + 1

    row, col = 2978, 3083
    pos = order(row - 1, col - 1)
    return val * pow(mul, pos - 1, mod) % mod


@timer
@print_result
def exercise2(arr):
    pass


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    exercise1(arr.copy())
    exercise2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
