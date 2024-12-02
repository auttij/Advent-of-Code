import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from aocHelpers.helpers import get_min_max
from collections import Counter


@timer
@print_result
def exercise1(arr):
    z = list(zip(*arr))
    s = 0
    for pair in zip(sorted(z[0]), sorted(z[1])):
        mi, ma = get_min_max(pair)
        s += ma - mi
    return s


@timer
@print_result
def exercise2(arr):
    l1, l2 = list(zip(*arr))
    counts = Counter(l2)
    return sum([i * counts[i] if i in counts else 0 for i in l1])


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_int_tuple_arr, args)
    exercise1(arr.copy())
    exercise2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
