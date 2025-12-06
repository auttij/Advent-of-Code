from sys import argv
from os import path
from aocHelpers.helpers import transpose
from aocHelpers.decorators import aoc_part
from aocHelpers.init import init
from itertools import groupby


def sum_rows(data, operators):
    # slower oneliner
    # sum([eval(f"{operators[i]}".join(line) for i, line in enumerate)])

    s = 0
    for i, v in enumerate(operators):
        if v == "+":
            s += sum(data[i])
        if v == "*":
            o = 1
            for val in data[i]:
                o *= val
            s += o
    return s


@aoc_part
def part1(arr):
    lines = [[] for i in range(len(arr[0].split()))]

    for line in arr[:-1]:
        for i, num in enumerate(line.split()):
            lines[i].append(int(num))
    return sum_rows(lines, (i for i in arr[-1].split()))


@aoc_part
def part2(arr):
    operators = (i for i in arr[-1].split())
    lines = transpose(arr[:-1])
    lines = ["".join(i).strip() for i in lines]

    groups = [
        [int(line) for line in group]
        for key, group in groupby(lines, key=lambda x: x != "")
        if key
    ]

    return sum_rows(groups, operators)


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
