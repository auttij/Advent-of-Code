from sys import argv
from os import path
from aocHelpers.decorators import aoc_part
from aocHelpers.init import init

@aoc_part
def part1(arr):
    dial = 50
    zeros = 0

    for line in arr:
        l = line[0]
        num = int(line[1:])

        if l == "L":
            dial = (dial - num) % 100
        if l == "R":
            dial = (dial + num) % 100
        if dial == 0:
            zeros += 1
    return zeros


@aoc_part
def part2(arr):
    dial = 50
    zeros = 0

    prev = 0
    for line in arr:
        l = line[0]
        num = int(line[1:])

        prev = dial

        zeros += num // 100
        num = num % 100


        if l == "L":
            dial = (dial - num)
            if prev != 0 and dial < 0:
                zeros += 1
            dial = dial % 100
        if l == "R":
            dial = (dial + num)
            if prev != 0 and dial > 100:
                zeros += 1
            dial = dial % 100
        if dial == 0:
            zeros += 1
    return zeros


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
