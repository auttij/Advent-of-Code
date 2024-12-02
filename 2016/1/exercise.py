import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init

dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]


@timer
@print_result
def exercise1(arr):
    y, x = 0, 0
    d = 0

    for instruction in arr[0].split(", "):
        lr = instruction[0]
        dist = int(instruction[1:])

        if lr == "R":
            d = (d + 1) % 4
        elif lr == "L":
            d = (d - 1) % 4
        y += dirs[d][0] * dist
        x += dirs[d][1] * dist
    return abs(y) + abs(x)


@timer
@print_result
def exercise2(arr):
    seen = []
    y, x = 0, 0
    d = 0

    for instruction in arr[0].split(", "):
        lr = instruction[0]
        dist = int(instruction[1:])

        if lr == "R":
            d = (d + 1) % 4
        elif lr == "L":
            d = (d - 1) % 4
        for i in range(dist):
            y += dirs[d][0]
            x += dirs[d][1]
            if (y, x) in seen:
                return abs(y) + abs(x)
            seen.append((y, x))
    return abs(y) + abs(x)


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    exercise1(arr.copy())
    exercise2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
