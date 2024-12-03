import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init


@timer
@print_result
def exercise1(num):
    ring = 0
    start = 0
    n = 1
    while n <= num:
        ring += 1
        start = n + 1
        n = (2 * ring + 1) ** 2

    mid_pos = [(i * 2 * ring) + (ring - 1) for i in range(4)]
    pos_on_ring = num - start
    dist = min([abs(pos_on_ring - i) for i in mid_pos])
    return ring + dist


@timer
@print_result
def exercise2(arr):
    # 1 -> 0
    # 2 -> 1, 0
    # 3 -> 2, 1, 0
    # 4 -> 3, 0
    # 5 -> 4, 3, 0

    pass


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_int_arr, args)
    exercise1(arr[0])
    exercise2(arr[0])


if __name__ == "__main__":
    main(argv[1:])
