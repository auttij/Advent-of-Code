import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from itertools import combinations, permutations, pairwise
from aocHelpers.helpers import bfs


def find_min_dist(arr, part2=False):
    pos = {}
    for y, row in enumerate(arr):
        for x, val in enumerate(row):
            if val not in [".", "#"]:
                pos[str(val)] = (y, x)

    distances = {}
    combos = list(combinations([f"{i}" for i in range(len(pos.keys()))], 2))

    def cmp(next, prev):
        return next != "#"

    for combo in combos:
        pos1, pos2 = combo
        dist = bfs(arr, pos[pos1], pos[pos2], cmp)
        distances[combo] = dist

    min_dist = 999999
    perms = permutations(
        [f"{i}" for i in range(1, len(pos.keys()))], len(pos.keys()) - 1
    )
    for perm in perms:
        if part2:
            perm = ("0",) + perm + ("0",)
        else:
            perm = ("0",) + perm
        dist = sum([distances[tuple(sorted(i))] for i in pairwise(perm)])
        if dist < min_dist:
            min_dist = dist
    return min_dist


@timer
@print_result
def exercise1(arr):
    return find_min_dist(arr)


@timer
@print_result
def exercise2(arr):
    return find_min_dist(arr, True)


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    exercise1(arr.copy())
    exercise2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
