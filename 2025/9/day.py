from sys import argv
from os import path
from aocHelpers.decorators import aoc_part
from aocHelpers.init import init
from itertools import combinations, pairwise


def get_area(rect):
    p1, p2 = rect
    return (abs(p2[0] - p1[0]) + 1) * (abs(p2[1] - p1[1]) + 1)


@aoc_part
def part1(data):
    return max(get_area((a, b)) for a in data for b in data)


@aoc_part
def part2(data):
    pairs = sorted(combinations(data, 2), key=get_area, reverse=True)
    for (x1, y1), (x2, y2) in pairs:
        # bounds of square
        bx1, bx2 = min(x1, x2), max(x1, x2)
        by1, by2 = min(y1, y2), max(y1, y2)

        # check if any line intersects with our square
        for (lx1, ly1), (lx2, ly2) in pairwise(data + [data[0]]):
            if not (
                max(lx1, lx2) <= bx1
                or bx2 <= min(lx1, lx2)
                or max(ly1, ly2) <= by1
                or by2 <= min(ly1, ly2)
            ):
                break
        else:
            return get_area(((x1, y1), (x2, y2)))


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
