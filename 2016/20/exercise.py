import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from functools import reduce


def get_ranges(arr):
    ranges = [arr[0]]
    for a, b in arr[1:]:
        i = 0
        while i < len(ranges):
            old_a, old_b = ranges[i]
            if a < old_a:
                break
            i += 1
        ranges.insert(i, (a, b))
        # print("before", ranges)
        i = 1
        while i < len(ranges):
            cur = ranges[i]
            prev = ranges[i - 1]
            if prev[1] + 1 >= cur[0]:
                ranges[i - 1] = (min(cur[0], prev[0]), max(cur[1], prev[1]))
                ranges.pop(i)
            else:
                i += 1
    return ranges


@timer
@print_result
def exercise1(arr):
    ranges = get_ranges(arr)
    return ranges[0][1] + 1


@timer
@print_result
def exercise2(arr):
    ranges = get_ranges(arr)
    count = 0
    limit = 4294967295
    for a, b in ranges[::-1]:
        count += limit - b
        limit = a - 1
    return count


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_int_tuple_arr, args)
    exercise1(arr.copy())
    exercise2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
