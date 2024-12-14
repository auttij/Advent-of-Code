from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init

import time


@timer
@print_result
def part1(arr):
    h = 103
    w = 101
    positions = []
    seconds = 100
    for px, py, vx, vy in arr:
        nx = (px + seconds * vx) % w
        ny = (py + seconds * vy) % h
        positions.append((nx, ny))

    Q = [0, 0, 0, 0]

    for px, py in positions:
        if py == ((h - 1) // 2) or px == ((w - 1) // 2):
            continue
        qy = py // ((h + 1) // 2)
        qx = px // ((w + 1) // 2)
        Q[2 * qy + qx] += 1
    return Q[0] * Q[1] * Q[2] * Q[3]


def pp(pos, w, h):
    rows = [["." for i in range(w)] for j in range(h)]
    for y in range(h):
        for x in range(w):
            if (y, x) in pos:
                rows[y][x] = "#"
    for line in rows:
        print("".join(line))


@timer
@print_result
def part2(arr):
    h = 103
    w = 101
    positions = [arr[i][:2] for i in range(len(arr))]

    i = 0
    while len(arr) != len(set(positions)):
        for j, (_, _, vx, vy) in enumerate(arr):
            ox, oy = positions[j]
            nx, ny = (ox + vx) % w, (oy + vy) % h
            positions[j] = (nx, ny)
        i += 1
    pp(positions, w, h)
    return i


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_int_tuple_arr, args)
    part1(arr.copy())
    part2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
