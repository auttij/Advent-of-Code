from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
import numpy as np

from math import gcd
from functools import reduce


def make_depth_arr(arr):
    base = [tuple(map(int, i.split(": "))) for i in arr]
    data = np.zeros(base[-1][0] + 1, dtype=int)
    for ind, dep in base:
        data[ind] = int(dep)
    return data


@timer
@print_result
def part1(arr):
    data = make_depth_arr(arr)

    severity = 0
    for i in range(len(data)):
        if data[i] != 0 and i % (2 * (data[i] - 1)) == 0:
            severity += i * data[i]

    return severity


def find_delay_simple(data):
    delay = 0
    while True:
        caught = False
        for i in range(len(data)):
            if data[i] != 0 and (i + delay) % (2 * (data[i] - 1)) == 0:
                caught = True
                break
        if not caught:
            return delay
        delay += 1


def lcm(a, b):
    return a * b // gcd(a, b)


def find_delay(layers):
    periods = [(i, 2 * (v - 1)) for i, v in layers.items()]
    L = reduce(lcm, (p for _, p in periods))
    for x in range(0, L, 2):
        if all((x + i) % p != 0 for i, p in periods):
            return x
    return None


@timer
@print_result
def part2(arr):
    data = make_depth_arr(arr)
    layers = {i: data[i] for i in range(len(data)) if data[i] != 0}
    return find_delay(layers)


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    part1(arr.copy())
    part2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
