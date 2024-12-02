import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from aocHelpers.helpers import md5_hash
from collections import deque


dirs = ["U", "D", "L", "R"]
dxy = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def bfs(grid, start, end, cmp, salt, part2=False):
    q = deque()
    q.append((start, []))
    longest = []
    printed = 0
    while q:
        pos, path = q.popleft()
        if not part2 and pos == end:
            return path
        if part2 and pos == end:
            if len(path) > len(longest):
                longest = path
            continue

        x, y = pos
        h = md5_hash("".join(path), salt)
        for i in range(len(dirs)):
            if cmp(h, i):
                dir = dirs[i]
                dx, dy = dxy[i]
                if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]):
                    q.append(((x + dx, y + dy), path + [dir]))
    if part2:
        return longest
    return []


@timer
@print_result
def exercise1(arr):
    size = 4
    grid = [[(x, y) for x in range(size)] for y in range(size)]

    def cmp(hash, idx):
        return hash[idx] in "bcdef"

    route = bfs(grid, (0, 0), (3, 3), cmp, arr)
    assert (len(route) > 0, "no result found")
    return "".join(route)


@timer
@print_result
def exercise2(arr):
    size = 4
    grid = [[(x, y) for x in range(size)] for y in range(size)]

    def cmp(hash, idx):
        return hash[idx] in "bcdef"

    route = bfs(grid, (0, 0), (3, 3), cmp, arr, part2=True)
    assert (len(route) > 0, "no result found")
    return len(route)


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    exercise1(arr[0])
    exercise2(arr[0])


if __name__ == "__main__":
    main(argv[1:])
