from sys import argv
from os import path
from aocHelpers.decorators import aoc_part
from aocHelpers.init import init


def taxi(ax, ay, bx, by):
    return abs(bx - ax) + abs(by - ay)


def find_closest(x, y, positions):
    dist = 9999
    ind = []

    for i, (px, py) in enumerate(positions):
        d = taxi(x, y, px, py)
        if d < dist:
            dist = d
            ind = [i]
        elif d == dist:
            ind.append(i)

    return ind


def is_closest(x, y, ind, positions):
    c = find_closest(x, y, positions)
    return len(c) == 1 and c[0] == ind


def get_infinite(positions):

    min_y, min_x = 999, 999
    max_y, max_x = 0, 0

    for x, y in positions:
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    infinite = set()
    for y in range(min_y - 1, max_y + 1):
        a = find_closest(min_x - 1, y, positions)
        if len(a) == 1:
            infinite.add(a[0])
        b = find_closest(max_x + 1, y, positions)
        if len(b) == 1:
            infinite.add(b[0])

    for x in range(min_x - 1, max_x + 1):
        a = find_closest(x, min_y - 1, positions)
        if len(a) == 1:
            infinite.add(a[0])
        b = find_closest(x, max_y + 1, positions)
        if len(b) == 1:
            infinite.add(b[0])
    return list(infinite)


def get_finite(positions):
    inf = get_infinite(positions)
    return [i for i in range(len(positions)) if i not in inf]


def get_area(ind, positions):
    area = 0
    stack = [positions[ind]]
    seen = set()

    while len(stack):
        x, y = stack.pop()
        if (x, y) in seen:
            continue
        seen.add((x, y))
        c = find_closest(x, y, positions)
        if len(c) != 1 or len(c) == 1 and c[0] != ind:
            continue
        area += 1

        neighbors = [
            [(nx, ny) for nx in range(x - 1, x + 2) if not (nx, ny) in seen]
            for ny in range(y - 1, y + 2)
        ]
        neighbors = [x for y in neighbors for x in y]
        stack = stack + neighbors
    return area


@aoc_part
def part1(arr):
    finite = get_finite(arr)
    top = 0
    for ind in finite:
        area = get_area(ind, arr)
        top = max(top, area)
    return top


def dist_sum(x, y, positions):
    return sum([taxi(x, y, px, py) for (px, py) in positions])


@aoc_part
def part2(arr):
    count = 0
    for y in range(50, 400):
        for x in range(50, 400):
            if dist_sum(x, y, arr) < 10000:
                count += 1
    return count


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
