import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from itertools import permutations, pairwise


def parse(input):
    def parse_line(line):
        words = line[:-1].split(" ")
        return [words[0], words[2], words[3], words[-1]]

    return [parse_line(i) for i in input]


def preprocess(parsed):
    out = {}
    for line in parsed:
        p1, operator, val, p2 = line
        key = "-".join(sorted([p1, p2]))
        if key not in out:
            out[key] = 0
        if operator == "gain":
            out[key] += int(val)
        else:
            out[key] -= int(val)
    return out


def calculate_sum(values, names):
    l1 = list(names) + list(names)[:1]
    out = 0
    for pair in pairwise(l1):
        key = "-".join(sorted(pair))
        out += values[key]
    return out


@timer
@print_result
def exercise1(arr):
    parsed = parse(arr)
    prepped = preprocess(parsed)
    names = list(set([i[0] for i in parsed]))
    perms = permutations(names)

    return max([calculate_sum(prepped, x) for x in perms])


def calculate_sum2(values, names):
    l1 = list(names) + list(names)[:1]
    l2 = []
    for pair in pairwise(l1):
        key = "-".join(sorted(pair))
        l2.append(values[key])
    minimum = min(l2)
    return sum(l2) - minimum


@timer
@print_result
def exercise2(arr):
    parsed = parse(arr)
    prepped = preprocess(parsed)
    names = list(set([i[0] for i in parsed]))
    perms = permutations(names)

    return max([calculate_sum2(prepped, x) for x in perms])


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    exercise1(arr.copy())
    exercise2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
