from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from aocHelpers.helpers import bfs


def get_grid():
    h, w = 71, 71
    return (0, 0), (70, 70), [["." for x in range(w)] for y in range(h)]


def process_bytes(grid, bytes):
    for x, y in bytes:
        grid[y][x] = "#"
    return grid


def cmp(nex, prev):
    return nex != "#"


@timer
@print_result
def part1(arr):
    start, end, grid = get_grid()
    grid = process_bytes(grid, arr[:1024])
    return bfs(grid, start, end, cmp)


def can_pass(steps):
    return steps != float("inf")


@timer
@print_result
def part2(arr):
    start, end, grid = get_grid()
    grid = process_bytes(grid, arr[:1024])
    i = 1024

    # check every 100 steps until can't pass
    passable = True
    while passable:
        new_grid = [row[:] for row in grid]
        for j in range(100):
            nx, ny = arr[i + j]
            new_grid[ny][nx] = "#"
        passable = can_pass(bfs(new_grid, start, end, cmp))
        if passable:
            grid = new_grid
            i += 100

    # check every step
    for x, y in arr[i:]:
        grid[y][x] = "#"
        if not can_pass(bfs(grid, start, end, cmp)):
            return f"{str(x)},{str(y)}"


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_int_tuple_arr, args)
    part1(arr.copy())
    part2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
