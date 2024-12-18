from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from aocHelpers.helpers import bfs


def get_grid(size):
    return (
        (0, 0),
        (size, size),
        [["." for x in range(size + 1)] for y in range(size + 1)],
    )


def process_bytes(grid, bytes):
    for x, y in bytes:
        grid[y][x] = "#"
    return grid


def cmp(nex, prev):
    return nex != "#"


@timer
@print_result
def part1(arr):
    start, end, grid = get_grid(70)
    grid = process_bytes(grid, arr[:1024])
    return bfs(grid, start, end, cmp)


@timer
@print_result
def part2(arr):
    def can_pass(grid):
        return bfs(grid, start, end, cmp) != float("inf")

    start, end, grid = get_grid(70)
    grid = process_bytes(grid, arr[:1024])
    i = 1024

    # check every x steps until can't pass
    x = 200
    passable = True
    while passable:
        new_grid = process_bytes([row[:] for row in grid], arr[i : i + x])
        passable = can_pass(new_grid)
        if passable:
            grid = new_grid
            i += x

    # check every step
    for x, y in arr[i:]:
        grid[y][x] = "#"
        if not can_pass(grid):
            return f"{str(x)},{str(y)}"


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_int_tuple_arr, args)
    part1(arr.copy())
    part2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
