import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from itertools import product


def neighbors(pos):
    dimensions = len(pos)
    combinations = product([-1, 0, 1], repeat=dimensions)
    for iter in combinations:
        if not any(iter):
            continue
        yield tuple(sum(i) for i in zip(iter, pos))


def pp(arr):
    print()
    for line in arr:
        print("".join(line))
    print()


def tick(prev):
    ymax = len(prev)
    xmax = len(prev[0])

    new = [["." for i in range(xmax)] for i in range(ymax)]
    for y in range(ymax):
        for x in range(xmax):
            old_val = prev[y][x]
            on_count = 0
            for ny, nx in neighbors([y, x]):
                if 0 <= ny < ymax and 0 <= nx < xmax:
                    nei_val = prev[ny][nx]
                    if nei_val == "#":
                        on_count += 1
            if old_val == "#" and on_count in [2, 3]:
                new[y][x] = "#"
            elif old_val == "." and on_count == 3:
                new[y][x] = "#"
    return new


@timer
@print_result
def exercise1(arr):
    grid = arr
    for i in range(100):
        # pp(grid)
        grid = tick(grid)
    return sum([i.count("#") for i in grid])


@timer
@print_result
def exercise2(arr):
    ymax = len(arr)
    xmax = len(arr[0])
    grid = [[arr[y][x] for x in range(xmax)] for y in range(ymax)]

    grid[0][0] = "#"
    grid[ymax - 1][0] = "#"
    grid[0][xmax - 1] = "#"
    grid[ymax - 1][xmax - 1] = "#"

    for i in range(100):
        # pp(grid)
        grid = tick(grid)
        grid[0][0] = "#"
        grid[ymax - 1][0] = "#"
        grid[0][xmax - 1] = "#"
        grid[ymax - 1][xmax - 1] = "#"
    return sum([i.count("#") for i in grid])


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    # exercise1(arr.copy())
    exercise2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
