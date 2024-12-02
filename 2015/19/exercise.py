import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from random import shuffle


def parse(arr):
    molecule = arr[-1]
    swaps = [i.split(" => ") for i in arr[:-2]]
    return swaps, molecule


@timer
@print_result
def exercise1(arr):
    swaps, molecule = parse(arr)

    seen = set()
    for input, output in swaps:
        l = len(input)
        for i in range(len(molecule) - l):
            if molecule[i : i + l] == input:
                seen.add(molecule[:i] + output + molecule[i + l :])
    return len(seen)


@timer
@print_result
def exercise2(arr):
    swaps, molecule = parse(arr)
    target = molecule
    steps = 0

    while target != "e":
        tmp = target
        for a, b in swaps:
            if b not in target:
                continue

            target = target.replace(b, a, 1)
            steps += 1

        if tmp == target:
            target = molecule
            steps = 0
            shuffle(swaps)

    return steps


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    exercise1(arr.copy())
    exercise2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
