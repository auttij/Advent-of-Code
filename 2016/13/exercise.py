import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from aocHelpers.helpers import bfs


def is_open(x, y, num):
    val = (x * x) + (3 * x) + (2 * x * y) + y + (y * y)
    return (val + num).bit_count() % 2 == 0


def is_wall(x, y, num):
    return not is_open(x, y, num)


def get_space(x, y, num):
    return "." if is_open(x, y, num) else "#"


@timer
@print_result
def exercise1(arr):
    num = int(arr)
    maze = [[get_space(x, y, num) for x in range(50)] for y in range(50)]

    def cmp(next, prev):
        return next == "."

    return bfs(maze, (1, 1), (39, 31), cmp)


@timer
@print_result
def exercise2(arr):
    num = int(arr)
    maze = [[get_space(x, y, num) for x in range(50)] for y in range(50)]

    def cmp(next, prev):
        return next == "."

    from collections import deque

    def bfs2(grid, start, end, cmp):
        can_reach_in_50 = 0

        q = deque()
        q.append((start, 0))
        seen = set()
        while q:
            pos, dist = q.popleft()
            if pos == end:
                return can_reach_in_50
            if pos in seen:
                continue

            if dist <= 50:
                can_reach_in_50 += 1
            seen.add(pos)
            x, y = pos
            for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                if (
                    0 <= x + dx < len(grid)
                    and 0 <= y + dy < len(grid[0])
                    and cmp(grid[x + dx][y + dy], grid[x][y])
                ):
                    q.append(((x + dx, y + dy), dist + 1))
        return float("inf")

    return bfs2(maze, (1, 1), (39, 31), cmp)


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    exercise1(arr[0])
    exercise2(arr[0])


if __name__ == "__main__":
    main(argv[1:])
