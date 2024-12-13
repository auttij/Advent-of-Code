from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init

import z3


def parse(arr):
    groups = []
    i = 0
    group = []
    for line in arr:
        if i < 3:
            group.append(line)
            i += 1
        else:
            groups.append(group)
            group = []
            i = 0
    groups.append(group)
    return groups


def solve(a, b, target, press_limit=None):
    a_cost, b_cost = 3, 1
    px, py = target
    ax, ay = a
    bx, by = b

    a_times = z3.Int("a_times")
    b_times = z3.Int("b_times")
    cost = z3.Int("cost")

    o = z3.Optimize()
    o.add(a_times * ax + b_times * bx == px)
    o.add(a_times * ay + b_times * by == py)
    if press_limit is not None:
        o.add(a_times <= press_limit)
        o.add(b_times <= press_limit)

    o.add(cost == a_times * a_cost + b_times * b_cost)
    o.minimize(cost)
    o.check()

    cost = o.model()[cost]

    return cost.as_long() if cost is not None else None


@timer
@print_result
def part1(arr):
    tokens = 0
    for a, b, prize in arr:
        cost = solve(a, b, prize, press_limit=100)
        if cost is not None:
            tokens += cost
    return tokens


@timer
@print_result
def part2(arr):
    offset = 10000000000000
    tokens = 0
    for a, b, prize in arr:
        px, py = prize
        target = (px + offset, py + offset)
        cost = solve(a, b, target)
        if cost is not None:
            tokens += cost

    return tokens


def main(args=None):
    asdf = init(path.dirname(__file__), inputs.read_to_int_tuple_arr, args)
    arr = parse(asdf)
    part1(arr.copy())
    part2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
