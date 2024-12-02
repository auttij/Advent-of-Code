import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
import re
import json


@timer
@print_result
def exercise1(arr):
    return sum([int(i.group()) for i in re.finditer(r"-?\d+", arr)])


@timer
@print_result
def exercise2(arr):
    def process(remaining):
        if isinstance(remaining, int):
            return remaining
        if isinstance(remaining, list):
            return sum([process(i) for i in remaining])
        elif isinstance(remaining, dict):
            if "red" in remaining.values():
                return 0
            return sum([process(v) for k, v in remaining.items()])
        else:
            return 0

    return process(arr)


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    exercise1("".join(arr))
    exercise2(json.loads(arr[0]))


if __name__ == "__main__":
    main(argv[1:])
