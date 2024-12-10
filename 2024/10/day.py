from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from aocHelpers.helpers import bfs


def cmp(nex, cur):
    return int(nex) - int(cur) == 1


def find_starts_ends(arr):
    zeroes = []
    nines = []
    for y, row in enumerate(arr):
        for x, val in enumerate(row):
            if val == "0":
                zeroes.append((y, x))
            if val == "9":
                nines.append((y, x))
    return zeroes, nines


@timer
@print_result
def part1(arr):
    starts, ends = find_starts_ends(arr)
    can_reach = 0
    for start in starts:
        can_reach += sum((bfs(arr, start, end, cmp) < 10 for end in ends))
    return can_reach


from collections import deque


# custom bfs without seen check, that counts amount of paths to each 9 dist
def bfs2(grid, start, end, cmp):
    out = 0
    q = deque()
    q.append((start, 0))
    while q:
        pos, dist = q.popleft()
        if dist > 9:
            continue
        if dist == 9:
            out += 1
        x, y = pos
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            if (
                0 <= x + dx < len(grid)
                and 0 <= y + dy < len(grid[0])
                and cmp(grid[x + dx][y + dy], grid[x][y])
            ):
                q.append(((x + dx, y + dy), dist + 1))
    return out


@timer
@print_result
def part2(arr):
    starts, _ = find_starts_ends(arr)
    return sum((bfs2(arr, start, "", cmp) for start in starts))


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    part1(arr.copy())
    part2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
