from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init


dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
markers = ["^", ">", "v", "<"]


def get_start(arr):
    for y, row in enumerate(arr):
        for x, val in enumerate(row):
            if val == "^":
                return y, x


@timer
@print_result
def part1(arr):
    arr = [list(row) for row in arr]
    start_pos = get_start(arr)
    arr, _ = solve(arr, start_pos)

    count = 0
    for line in arr:
        for val in line:
            if val in markers:
                count += 1
    return count


def solve(arr, start_pos):
    yi, xi = start_pos

    chosen_dir = 0
    seen_count = 0
    seen = set()
    while True:
        if (yi, xi) not in seen:
            seen.add((yi, xi))
        elif seen_count < 1000:
            seen_count += 1
        else:
            return arr, True

        yn, xn = dirs[chosen_dir]
        ny, nx = yi + yn, xi + xn

        if not (0 <= ny < len(arr) and 0 <= nx < len(arr[0])):
            break
        n = arr[ny][nx]
        if n == markers[chosen_dir]:
            return arr, True
        elif n == "#":
            ny -= dirs[chosen_dir][0]
            nx -= dirs[chosen_dir][1]
            chosen_dir = (chosen_dir + 1) % len(dirs)
        arr[yi][xi] = markers[chosen_dir]
        yi, xi = ny, nx
        arr[yi][xi] == "X"
    arr[yi][xi] = markers[chosen_dir]
    return arr, False


@timer
@print_result
def part2(arr):
    arr = [list(row) for row in arr]
    arr_copy = [[i for i in line[::]] for line in arr[::]]
    start_pos = get_start(arr)
    yi, xi = start_pos
    solved, _ = solve(arr, start_pos)

    blockers = 0
    for y, row in enumerate(solved):
        for x, val in enumerate(row):
            if (y == yi and x == xi) or (val not in markers):
                continue

            ac = [[i for i in line[::]] for line in arr_copy[::]]
            ac[y][x] = "#"

            ac, loop = solve(ac, start_pos)
            if loop:
                blockers += 1
    return blockers


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    part1(arr.copy())
    part2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
