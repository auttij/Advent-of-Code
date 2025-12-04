from sys import argv
from os import path
from aocHelpers.decorators import aoc_part
from aocHelpers.init import init


def neigh(x, y, arr):
    max_y = len(arr)
    max_x = len(arr[0])
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if dy == 0 and dx == 0:
                continue
            ny = y + dy
            nx = x + dx
            if 0 <= ny < max_y and 0 <= nx < max_x:
                yield arr[ny][nx]


def get_movable(arr):
    movable = []
    for y, line in enumerate(arr):
        for x, val in enumerate(line):
            if val == ".":
                continue
            comp = list(neigh(x, y, arr)).count("@")
            if comp < 4:
                movable.append((y, x))
    return movable


@aoc_part
def part1(arr):
    return len(get_movable(arr))


@aoc_part
def part2(arr):
    moved = 0
    movable = get_movable(arr)
    while len(movable):
        for y, x in movable:
            arr[y][x] = "." 
        moved += len(movable)
        movable = get_movable(arr)
    return moved


def parse_input(raw):
    return [list(i) for i in raw.splitlines()]


def main(args=None):
    raw = init(path.dirname(__file__), args)

    data1 = parse_input(raw)
    part1(data1)

    data2 = parse_input(raw)
    part2(data2)


if __name__ == "__main__":
    main(argv[1:])
