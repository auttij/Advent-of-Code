from sys import argv
from os import path
from aocHelpers.decorators import aoc_part
from aocHelpers.init import init
import string

def get_reactions():
    pairs = map(lambda x: "".join(x), zip(string.ascii_lowercase, string.ascii_uppercase))
    pairs2 = map(lambda x: "".join(x), zip(string.ascii_uppercase, string.ascii_lowercase))
    return list(pairs) + (list(pairs2))

def react(polymer, reactions):
    cur = polymer
    prev = None
    while prev != cur:
        prev = cur
        for i in reactions:
            cur = cur.replace(i, "")
    return len(cur)


@aoc_part
def part1(arr):
    reactions = get_reactions()
    return react(arr, reactions)

@aoc_part
def part2(arr):
    reactions = get_reactions()
    lowest = 999999999

    for letter in string.ascii_lowercase:
        polymer = arr.replace(letter, "")
        polymer = polymer.replace(letter.upper(), "")
        res = react(polymer, reactions)
        if res < lowest:
            lowest = res
    return lowest




def parse_input(raw):
    return raw


def main(args=None):
    raw = init(path.dirname(__file__), args)

    data1 = parse_input(raw)
    part1(data1)

    data2 = parse_input(raw)
    part2(data2)


if __name__ == "__main__":
    main(argv[1:])
