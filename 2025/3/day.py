from sys import argv
from os import path
from aocHelpers.decorators import aoc_part
from aocHelpers.init import init


def find_joltage(bank, k):
    bank = list(bank)
    result = []

    start = 0
    while k > 0:
        # Last index to choose with enough digits left
        end = len(bank) - k + 1

        max_digit = max(bank[start:end])
        idx = bank.index(max_digit, start, end)

        result.append(max_digit)

        start = idx + 1
        k -= 1

    return int("".join(result))


def total_joltage(arr, k):
    s = 0
    for bank in arr:
        s += find_joltage(bank, k)
    return s


@aoc_part
def part1(arr):
    return total_joltage(arr, 2)


@aoc_part
def part2(arr):
    return total_joltage(arr, 12)


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
