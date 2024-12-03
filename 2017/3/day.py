from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init


def nof_rings(num):
    rings = {}
    ring = 0
    start = 1
    n = 1
    while n < num:
        rings[(start, n)] = ring
        ring += 1
        start = n + 1
        n = (2 * ring + 1) ** 2
    return ring, start, rings


@timer
@print_result
def part1(num):
    ring, start, _ = nof_rings(num)
    mid_pos = [(i * 2 * ring) + (ring - 1) for i in range(4)]
    pos_on_ring = num - start
    dist = min([abs(pos_on_ring - i) for i in mid_pos])
    return ring + dist


from itertools import count
from collections import defaultdict


def sum_spiral():
    a, i, j = defaultdict(int), 0, 0
    a[0, 0] = 1
    sn = lambda i, j: sum(
        a[k, l] for k in range(i - 1, i + 2) for l in range(j - 1, j + 2)
    )
    for s in count(1, 2):
        for _ in range(s):
            i += 1
            a[i, j] = sn(i, j)
            yield a[i, j]
        for _ in range(s):
            j -= 1
            a[i, j] = sn(i, j)
            yield a[i, j]
        for _ in range(s + 1):
            i -= 1
            a[i, j] = sn(i, j)
            yield a[i, j]
        for _ in range(s + 1):
            j += 1
            a[i, j] = sn(i, j)
            yield a[i, j]


@timer
@print_result
def part2(num):
    for x in sum_spiral():
        if x > num:
            return x


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_int_arr, args)
    part1(arr[0])
    part2(arr[0])


if __name__ == "__main__":
    main(argv[1:])
