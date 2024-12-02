import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from aocHelpers.helpers import transpose


def rotate(rect, rot, row=None, col=None):
    if row != None:
        rect[row] = rect[row][-rot:] + rect[row][:-rot]
    elif col != None:
        rect = transpose(rect)
        rect[col] = rect[col][-rot:] + rect[col][:-rot]
        rect = transpose(rect)
    return rect


@timer
@print_result
def exercise1(arr):
    rect = [["." for i in range(50)] for i in range(6)]
    for instruction in arr:
        if instruction[:4] == "rect":
            rx, ry = instruction.split(" ")[-1].split("x")
            for y in range(int(ry)):
                for x in range(int(rx)):
                    rect[y][x] = "#"
        else:
            splt = instruction.split(" ")
            row_or_col = splt[1]
            rot = int(splt[-1])
            rc = int(splt[2].split("=")[-1])
            if row_or_col == "row":
                rect = rotate(rect, rot, row=rc)
            else:
                rect = rotate(rect, rot, col=rc)

    print("part2:")
    for line in rect:
        print("".join(line))
    return sum([i.count("#") for i in rect])


@timer
@print_result
def exercise2(arr):
    pass


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    exercise1(arr.copy())
    # exercise2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
