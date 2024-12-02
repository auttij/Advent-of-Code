import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init


@timer
@print_result
def exercise1(arr):
    input = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }
    for aunt, row in enumerate(arr, start=1):
        parts = row.split(", ")
        matching = True
        for part in parts:
            splt = part.split(": ")
            key = splt[-2]
            val = splt[-1]

            if input[key] != int(val):
                matching = False
                break

        if matching:
            return aunt

    pass


@timer
@print_result
def exercise2(arr):
    input = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }

    def compare_input(input, key, val):
        if key in ["cats", "trees"]:
            return input[key] < val
        elif key in ["goldfish", "pomeranians"]:
            return input[key] > val
        else:
            return input[key] == val

    for aunt, row in enumerate(arr, start=1):
        parts = row.split(", ")
        matching = True
        for part in parts:
            splt = part.split(": ")
            key = splt[-2]
            val = splt[-1]

            if not compare_input(input, key, int(val)):
                matching = False
                break

        if matching:
            return aunt

    pass


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    exercise1(arr.copy())
    exercise2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
