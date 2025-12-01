from sys import argv
from os import path
from aocHelpers.decorators import aoc_part
from aocHelpers.init import init


@aoc_part
def part1(arr):
    dial = 50
    zeros = 0

    for dir, val in arr:
        sign = {"L": -1, "R": 1}
        dial = (dial + sign[dir] * val) % 100
        if dial == 0:
            zeros += 1
    return zeros


@aoc_part
def part2(arr):
    dial = 50
    zeros = 0
    prev = 0

    for dir, val in arr:
        prev = dial

        zeros += val // 100  # rotations over 100 hit 0 multiple times
        val = val % 100

        sign = {"L": -1, "R": 1}
        dial = dial + sign[dir] * val

        if prev != 0 and not 0 <= dial <= 100:
            zeros += 1

        dial = dial % 100
        if dial == 0:
            zeros += 1
    return zeros


def parse_input(raw):
    return [(val[0], int(val[1:])) for val in raw.splitlines()]


def main(args=None):
    raw = init(path.dirname(__file__), args)

    data1 = parse_input(raw)
    part1(data1)

    data2 = parse_input(raw)
    part2(data2)


if __name__ == "__main__":
    main(argv[1:])
