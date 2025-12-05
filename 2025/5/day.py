from sys import argv
from os import path
from aocHelpers.decorators import aoc_part
from aocHelpers.init import init


@aoc_part
def part1(data):
    fresh, ing = data
    c = 0

    for i in ing:
        for a, b in fresh:
            if a <= i <= b:
                c += 1
                break

    return c


@aoc_part
def part2(data):
    fresh, _ = data

    intervals = sorted(fresh, key=lambda i: i[0])

    result = [list(intervals[0])]
    for interval in intervals[1:]:
        if interval[0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], interval[1])
        else:
            result.append(list(interval))

    count = 0
    for a, b in result:
        count += b - a + 1
    return count


def parse_input(raw):
    a, b = raw.split("\n\n")
    fresh = [tuple(map(int, line.split("-"))) for line in a.split("\n")]
    ing = list(map(int, b.split("\n")))
    return (fresh, ing)


def main(args=None):
    data = init(path.dirname(__file__), args)

    data1 = parse_input(data)
    part1(data1)

    data2 = parse_input(data)
    part2(data2)


if __name__ == "__main__":
    main(argv[1:])
