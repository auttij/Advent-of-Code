import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init


def is_trap(left, center, right):
    return (
        (left and center and not right)
        or (not left and center and right)
        or (left and not center and not right)
        or (not left and not center and right)
    )


def determine_tile(previous_row, pos):
    positions = (pos + i for i in (-1, 0, 1))
    traps = (
        previous_row[p] == "^" if 0 <= p < len(previous_row) else False
        for p in positions
    )
    return "^" if is_trap(*traps) else "."


def calculate_safe_tiles(row, row_count):
    safe = 0
    i = 0
    while i < row_count:
        safe += row.count(".")
        new_row = "".join([determine_tile(row, i) for i in range(len(row))])
        row = new_row
        i += 1
    return safe


@timer
@print_result
def exercise1(row):
    return calculate_safe_tiles(row, 40)


@timer
@print_result
def exercise2(row):
    return calculate_safe_tiles(row, 400000)


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    exercise1(arr[0])
    exercise2(arr[0])


if __name__ == "__main__":
    main(argv[1:])
