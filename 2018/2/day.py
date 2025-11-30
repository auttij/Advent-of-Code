from sys import argv
from os import path
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init

from collections import Counter


@timer
@print_result
def part1(arr):
    twos = 0
    threes = 0

    for line in arr:
        c = Counter(line)
        if 2 in c.values():
            twos += 1
        if 3 in c.values():
            threes += 1

    return twos * threes


@timer
@print_result
def part2(arr):
    def diff(s1, s2):
        out = []
        for i, val in enumerate(s1):
            if s2[i] != val:
                out.append([val, s2[i]])
        return out

    for i, s1 in enumerate(arr):
        for s2 in arr[i:]:
            d = diff(s1, s2)
            if len(d) == 1:
                out = "".join([val for j, val in enumerate(s1) if val == s2[j]])
                return out


def parse_input(raw):
    return raw.splitlines()


def main(args=None):
    raw = init(path.dirname(__file__), args)

    data1 = parse_input(raw)
    part1(data1)

    data2 = parse_input(raw)
    part2(data2)


if __name__ == "__main__":
    main(argv[1:])
