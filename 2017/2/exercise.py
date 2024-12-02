import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from itertools import combinations


def diff(arr):
    return max(arr) - min(arr)


@timer
@print_result
def exercise1(arr):
    return sum(map(diff, arr))


@timer
@print_result
def exercise2(arr):
    s = 0
    for line in arr:
        for a, b in combinations(line, 2):
            if a % b == 0:
                s += a // b
            elif b % a == 0:
                s += b // a
    return s


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_int_tuple_arr, args)
    exercise1(arr.copy())
    exercise2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
