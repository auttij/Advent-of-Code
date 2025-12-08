from sys import argv
from os import path
from aocHelpers.decorators import aoc_part
from aocHelpers.init import init
from math import sqrt
from collections import defaultdict, Counter, deque


def line_distance(p1, p2):
    return sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2 + (p2[2] - p1[2]) ** 2)


def distances(data):
    d = []
    for i, p1 in enumerate(data):
        for j, p2 in enumerate(data):
            if i > j:
                distance = line_distance(p1, p2)
                d.append((distance, i, j))
    return sorted(d)


def union_find(distances, data, part):
    UF = {i: i for i in range(len(data))}

    def find(x):
        if x == UF[x]:
            return x
        UF[x] = find(UF[x])
        return UF[x]

    def mix(x, y):
        UF[find(x)] = find(y)

    p1 = 0
    p2 = 0

    connections = 0
    for t, (_d, i, j) in enumerate(distances):
        if part == 1 and t == 1000:
            sizes = defaultdict(int)
            for x in range(len(data)):
                sizes[find(x)] += 1
            s = sorted(sizes.values())
            return s[-1] * s[-2] * s[-3]

        if find(i) != find(j):
            connections += 1
            if part == 2 and connections == len(data) - 1:
                return data[i][0] * data[j][0]
            mix(i, j)

    return p1, p2


@aoc_part
def part1(data):
    d = distances(data)
    return union_find(d, data, 1)


@aoc_part
def part2(data):
    d = distances(data)
    return union_find(d, data, 2)


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
