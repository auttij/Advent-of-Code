from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from itertools import product


def solve(line, possible_operators):
    target, *rest = line
    p = list(product(possible_operators, repeat=len(rest) - 1))
    for iterations, operators in enumerate(p):
        s = rest[0]
        for i, operator in enumerate(operators, start=1):
            if operator == "p":
                s += rest[i]
            elif operator == "m":
                s *= rest[i]
            elif operator == "c":
                s = int(f"{s}{rest[i]}")
        if s == target:
            return target, iterations
    return 0, len(p)


@timer
@print_result
def part1(arr):
    out = 0
    for line in arr:
        out += solve(line, "mp")[0]
    return out


@timer
@print_result
def part2(arr):
    out = 0
    total_iterations = 0
    for line in arr:
        result, i = solve(line, "mp")
        if not result:
            result, i2 = solve(line, "cpm")
            total_iterations += i2
        out += result
        total_iterations += i
    print(f"{total_iterations = }")
    return out


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_int_tuple_arr, args)
    part1(arr.copy())
    part2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
