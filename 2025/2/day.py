from sys import argv
from os import path
from aocHelpers.decorators import aoc_part
from aocHelpers.init import init


def check_id_list(data, check_fn):
    sum = 0
    for a, b in data:
        for i in range(int(a), int(b) + 1):
            if not check_fn(str(i)):
                sum += i
    return sum


@aoc_part
def part1(arr):
    def is_valid(id):
        l = len(id)
        return id[: l // 2] != id[l // 2 :]

    return check_id_list(arr, is_valid)


@aoc_part
def part2(arr):
    def is_valid(id):
        for i in range(1, len(id) // 2 + 1):
            if not len(id) % i and id.count(id[:i]) == (len(id) / i):
                return False
        return True

    return check_id_list(arr, is_valid)


def parse_input(raw):
    return [pair.split("-") for pair in raw.split(",")]


def main(args=None):
    raw = init(path.dirname(__file__), args)

    data1 = parse_input(raw)
    part1(data1)

    data2 = parse_input(raw)
    part2(data2)


if __name__ == "__main__":
    main(argv[1:])
