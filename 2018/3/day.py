from sys import argv
from os import path
from aocHelpers.decorators import aoc_part
from aocHelpers.init import init


@aoc_part
def part1(arr):
    fabric = {}
    for id, left, top, width, height in arr:
        for x in range(left, left + width):
            for y in range(top, top + height):
                if (y,x) not in fabric:
                    fabric[(y,x)] = 0
                fabric[(y,x)] += 1
    return len([i for i in fabric.values() if i > 1])


@aoc_part
def part2(arr):
    fabric = {}
    sizes = {}

    for id, left, top, width, height in arr:
        sizes[id] = width * height
        for x in range(left, left + width):
            for y in range(top, top + height):
                if (y,x) not in fabric:
                    fabric[(y,x)] = []
                fabric[(y,x)].append(id)

    ones = [i for i in fabric.values() if len(i) == 1]
    flat = [x for y in ones for x in y]
    for id in range(1, len(arr) + 1):
        if flat.count(id) == sizes[id]:
            return id


def parse_input(raw):
    import re
    return [tuple(map(int, re.findall(r"-?\d+", line))) for line in raw.splitlines()]


def main(args=None):
    raw = init(path.dirname(__file__), args)

    data1 = parse_input(raw)
    part1(data1)

    data2 = parse_input(raw)
    part2(data2)


if __name__ == "__main__":
    main(argv[1:])
