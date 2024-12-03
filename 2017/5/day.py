from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init


@timer
@print_result
def part1(arr):
    cmd_idx = 0
    jumps = 0
    while 0 <= cmd_idx < len(arr):
        pos = cmd_idx
        jumps += 1
        cmd_idx += arr[pos]
        if 0 <= pos < len(arr):
            arr[pos] += 1

    return jumps


@timer
@print_result
def part2(arr):
    cmd_idx = 0
    jumps = 0
    while 0 <= cmd_idx < len(arr):
        jumps += 1
        pos = cmd_idx
        offset = arr[pos]
        cmd_idx += offset
        if offset >= 3:
            arr[pos] -= 1
        else:
            arr[pos] += 1

    return jumps


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_int_arr, args)
    part1(arr.copy())
    part2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
