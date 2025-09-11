from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init


@timer
@print_result
def part1(arr):
    score = 0
    current = 0
    garbage = False
    ignore = False

    for char in arr:
        if ignore:
            ignore = False
            continue

        if char == "!":
            ignore = True
            continue

        if garbage:
            if char == ">":
                garbage = False
            continue

        if char == "<":
            garbage = True
            continue

        if char == "{":
            current += 1
            continue

        if char == "}":
            score += current
            current -= 1
            continue
        
    return score


@timer
@print_result
def part2(arr):
    garbage_count = 0
    garbage = False
    ignore = False

    for char in arr:
        if ignore:
            ignore = False
            continue

        if char == "!":
            ignore = True
            continue

        if garbage:
            if char == ">":
                garbage = False
            else:
                garbage_count += 1
            continue

        if char == "<":
            garbage = True
            continue
        
    return garbage_count


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str, args)
    part1(arr)
    part2(arr)


if __name__ == "__main__":
    main(argv[1:])
