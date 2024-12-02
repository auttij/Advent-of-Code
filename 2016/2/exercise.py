import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init


@timer
@print_result
def exercise1(arr):
    numpad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    code = []

    y, x = 1, 1
    for line in arr:
        for inst in line:
            if inst == "L":
                x = max(0, x - 1)
            if inst == "R":
                x = min(2, x + 1)
            if inst == "U":
                y = max(0, y - 1)
            if inst == "D":
                y = min(2, y + 1)
        code.append(numpad[y][x])
    return code


@timer
@print_result
def exercise2(arr):
    numpad = [
        [".", ".", "1", "*", "*"],
        [".", "2", "3", "4", "*"],
        ["5", "6", "7", "8", "9"],
        [",", "A", "B", "C", "-"],
        [",", ",", "D", "-", "-"],
    ]
    code = []

    #          x
    #         02
    #      11 12 13
    # y 20 21 22 23 24
    #      31 32 33
    #         42

    y, x = 2, 0
    for line in arr:
        for inst in line:
            if inst == "L":
                x = max(0, x - 1)
                if numpad[y][x] in [".", ","]:
                    x += 1

            if inst == "R":
                x = min(4, x + 1)
                if numpad[y][x] in ["*", "-"]:
                    x -= 1

            if inst == "U":
                y = max(0, y - 1)
                if numpad[y][x] in [".", "*"]:
                    y += 1

            if inst == "D":
                y = min(4, y + 1)
                if numpad[y][x] in [",", "-"]:
                    y -= 1
            # print(inst, y, x, numpad[y][x])
        # print("-------")
        code.append(numpad[y][x])
    return "".join(code)


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    exercise1(arr.copy())
    exercise2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
