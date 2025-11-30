from sys import argv
from os import path
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init


@timer
@print_result
def part1(arr):
    pass


@timer
@print_result
def part2(arr):
    pass


def parse_input(raw):
    # arr
    # return raw.splitlines()

    # int arr
    # return list(map(int, raw.splitlines()))

    # str pairs
    # return [line.split() for line in raw.splitlines()]

    # select numbers from input
    # import re
    # return [tuple(map(int, re.findall(r"-?\d+", line))) for line in raw.splitlines()]

    return raw


def main(args=None):
    raw = init(path.dirname(__file__), args)

    data1 = parse_input(raw)
    part1(data1)

    data2 = parse_input(raw)
    part2(data2)


if __name__ == "__main__":
    main(argv[1:])
