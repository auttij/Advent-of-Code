import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from itertools import combinations


def get_combos(inputs, min_length_combos=False):
    combos = []
    for length in range(1, len(inputs) + 1):
        combos.extend(
            (
                tuple(combo)
                for combo in combinations(inputs, length)
                if sum(combo) == 150
            )
        )
        if min_length_combos and combos:
            break
    return combos


@timer
@print_result
def exercise1(arr):
    return len(get_combos(arr))


@timer
@print_result
def exercise2(arr):
    return len(get_combos(arr, True))


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_int_arr, args)
    exercise1(arr.copy())
    exercise2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
