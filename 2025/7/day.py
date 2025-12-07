from sys import argv
from os import path
from aocHelpers.decorators import aoc_part
from aocHelpers.init import init


def track_beams(data):
    splits = 0
    beams = [0] * len(data[0])
    beams[data[0].index("S")] = 1

    for line in data[2::2]:
        new_beams = [0] * len(line)
        for i, ch in enumerate(line):
            if ch == "^":
                new_beams[i - 1] += beams[i]
                new_beams[i + 1] += beams[i]
                if beams[i]:
                    splits += 1
            else:
                new_beams[i] += beams[i]
        beams = new_beams
    return splits, sum(new_beams)


@aoc_part
def part1(data):
    return track_beams(data)[0]


@aoc_part
def part2(data):
    return track_beams(data)[1]


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
