from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from collections import defaultdict


def calc_dist(instructions):
    c = defaultdict(int)
    for dir in instructions:
        c[dir] += 1

    opposites = [("n", "s"), ("ne", "sw"), ("nw", "se")]
    for a, b in opposites:
        if c[a] > c[b]:
            c[a] -= c[b]
            c[b] = 0
        else:
            c[b] -= c[a]
            c[a] = 0

    same_y = [("ne", "nw", "n"), ("se", "sw", "s")]
    for a, b, m in same_y:
        # print(f"{a}: {c[a]}, {b}: {c[b]}, {m}: {c[m]}")
        min_val = min(c[a], c[b])
        c[m] += min_val
        c[a] -= min_val
        c[b] -= min_val

    turns = [("ne", "s", "se"), ("se", "n", "ne"), ("nw", "s", "sw"), ("sw", "n", "nw")]
    for a, b, m in turns:
        min_val = min(c[a], c[b])
        c[m] += min_val
        c[a] -= min_val
        c[b] -= min_val

    return sum(c.values())


@timer
@print_result
def part1(arr):
    return calc_dist(arr[0].split(","))


@timer
@print_result
def part2(arr):
    best = 0
    instructions = arr[0].split(",")
    for i in range(len(instructions)):
        dist = calc_dist(instructions[: i + 1])
        if dist > best:
            best = dist
    return best


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    part1(arr.copy())
    part2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
