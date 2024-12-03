from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from collections import Counter


@timer
@print_result
def part1(arr):
    s = 0
    for line in arr:
        c = Counter(line.split())
        if c.most_common(1)[0][1] == 1:
            s += 1
    return s


@timer
@print_result
def part2(arr):
    s = 0
    for line in arr:
        asd = set()
        copy = False
        for word in line.split():
            sw = "".join(sorted(word))
            if sw not in asd:
                asd.add(sw)
            else:
                copy = True
        if not copy:
            s += 1
    return s


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    part1(arr.copy())
    part2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
