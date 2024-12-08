from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from itertools import combinations


def solve(arr, part2=False):
    node_pos = {}
    for y, row in enumerate(arr):
        for x, val in enumerate(row):
            if val == ".":
                continue
            if val not in node_pos:
                node_pos[val] = []
            node_pos[val].append((y, x))

    h = len(arr)
    w = len(arr[0])

    n1, n2 = set(), set()
    for positions in node_pos.values():
        for i, j in combinations(positions, 2):
            dy, dx = j[0] - i[0], j[1] - i[1]
            y, x, s = *j, 0
            while 0 <= x < w and 0 <= y < h:
                if s == 1:
                    n1.add((y, x))
                n2.add((y, x))
                y, x, s = y + dy, x + dx, s + 1
            y, x, s = *i, 0
            while 0 <= x < w and 0 <= y < h:
                if s == 1:
                    n1.add((y, x))
                n2.add((y, x))
                y, x, s = y - dy, x - dx, s + 1
    if part2:
        return len(n2)
    return len(n1)


@timer
@print_result
def part1(arr):
    return solve(arr)


@timer
@print_result
def part2(arr):
    return solve(arr, True)


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    part1(arr.copy())
    part2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
