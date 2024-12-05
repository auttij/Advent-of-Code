from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init


def parse(arr):
    rules = []
    pages = []

    mid = False
    for line in arr:
        if len(line) == 0:
            mid = True
        elif not mid:
            parts = tuple(map(int, line.split("|")))
            rules.append(parts)
        else:
            parts = list(map(int, line.split(",")))
            pages.append(parts)
    return rules, pages


def is_ordered(rules, row):
    ordered = True
    for rule in rules:
        x, y = rule
        if x in row and y in row:
            xi = row.index(x)
            yi = row.index(y)
            if yi < xi:
                ordered = False
                break
    return ordered


def re_order(rules, row):
    ordered = False
    while not ordered:
        for rule in rules:
            x, y = rule
            if x in row and y in row:
                xi = row.index(x)
                yi = row.index(y)
                if yi < xi:
                    row[xi], row[yi] = row[yi], row[xi]
        ordered = is_ordered(rules, row)
    return row


@timer
@print_result
def part1(rules, pages):
    s = 0
    for row in pages:
        if is_ordered(rules, row):
            s += row[len(row) // 2]
    return s


@timer
@print_result
def part2(rules, pages):
    s = 0
    for row in pages:
        if not is_ordered(rules, row):
            new_row = re_order(rules, row)
            s += new_row[len(row) // 2]
    return s


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    rules, pages = parse(arr)
    part1(rules.copy(), pages.copy())
    part2(rules.copy(), pages.copy())


if __name__ == "__main__":
    main(argv[1:])
