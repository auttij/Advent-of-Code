import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from functools import reduce
from itertools import pairwise


def is_safe(line):
    pairs = [x - y for x, y in pairwise(line)]
    mi = min(pairs)
    ma = max(pairs)

    # no 0 diff
    if 0 in pairs:
        return False

    # all positive (increasing) or all negative (decreasing)
    if ma > 0 and mi < 0:
        return False

    # no jumps bigger than 3
    if ma > 3 or mi < -3:
        return False
    return True


@timer
@print_result
def exercise1(arr):
    return sum([is_safe(l) for l in arr])


@timer
@print_result
def exercise2(arr):
    safe_count = 0
    for line in arr:
        if is_safe(line):
            safe_count += 1
            continue

        for i in range(len(line)):
            if is_safe(line[:i] + line[i + 1 :]):
                safe_count += 1
                break
    return safe_count


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_int_tuple_arr, args)
    exercise1(arr.copy())
    exercise2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
