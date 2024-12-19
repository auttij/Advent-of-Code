from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from functools import lru_cache


@lru_cache
def solve(remaining):
    if len(remaining) == 0:
        return 1
    return sum(
        (solve(remaining[len(p) :]) for p in patterns if remaining[: len(p)] == p)
    )


@timer
@print_result
def part1():
    return sum((solve(target) > 0 for target in targets))


@timer
@print_result
def part2():
    return sum((solve(target) for target in targets))


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)

    global patterns, targets
    patterns = tuple([i.strip() for i in arr[0].split(",")])
    targets = arr[2:]

    part1()
    part2()


if __name__ == "__main__":
    main(argv[1:])
