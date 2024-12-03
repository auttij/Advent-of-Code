from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
import re


def parse(arr):
    r = re.compile("mul\\((\\d+),(\\d+)\\)")
    do = re.compile("do\\(\\)")
    dont = re.compile("don't\\(\\)")

    matches = [(m.groups(), m.span()[0]) for m in r.finditer(arr)]
    dos = [("do", m.span()[0]) for m in do.finditer(arr)]
    donts = [("dont", m.span()[0]) for m in dont.finditer(arr)]

    out = matches + dos + donts
    out = list(map(lambda x: x[0], sorted(out, key=lambda x: x[1])))
    return out


@timer
@print_result
def part1(arr):
    s = 0
    for ins in arr:
        if isinstance(ins, tuple):
            x, y = ins
            s += int(x) * int(y)
    return s


@timer
@print_result
def part2(arr):
    s = 0
    enabled = True
    for ins in arr:
        if ins == "do":
            enabled = True
        elif ins == "dont":
            enabled = False
        elif enabled:
            x, y = ins
            s += int(x) * int(y)
    return s


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str, args)
    parsed = parse(arr)
    part1(parsed)
    part2(parsed)


if __name__ == "__main__":
    main(argv[1:])
