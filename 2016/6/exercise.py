import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from aocHelpers.helpers import transpose
from collections import Counter


@timer
@print_result
def exercise1(arr):
    t = transpose(arr)
    res = []
    for row in t:
        c = Counter(row)
        res.append(c.most_common(1)[0][0])
    return "".join(res)


@timer
@print_result
def exercise2(arr):
    t = transpose(arr)
    res = []
    for row in t:
        c = Counter(row)
        res.append(c.most_common(26)[-1][0])
    return "".join(res)


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    exercise1(arr.copy())
    exercise2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
