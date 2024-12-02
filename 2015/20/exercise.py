import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from functools import reduce
from math import sqrt


def factors(n):
    step = 2 if n % 2 else 1
    return set(
        reduce(
            list.__add__,
            ([i, n // i] for i in range(1, int(sqrt(n)) + 1, step) if n % i == 0),
        )
    )


def present_count(house_number):
    return 10 * sum((i for i in factors(house_number)))


@timer
@print_result
def exercise1(limit):
    for i in range(800000, 1000000):
        presents = present_count(i)
        if presents > limit:
            return i


def factors2(n):
    step = 2 if n % 2 else 1
    f = set(
        reduce(
            list.__add__,
            ([i, n // i] for i in range(1, int(sqrt(n)) + 1, step) if n % i == 0),
        )
    )
    return (i for i in f if n / i <= 50)


def present_count2(house_number):
    return 11 * sum((i for i in factors2(house_number)))


@timer
@print_result
def exercise2(limit):
    for i in range(800000, 1000000):
        presents = present_count2(i)
        if presents > limit:
            return i


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str, args)
    exercise1(int(arr))
    exercise2(int(arr))


if __name__ == "__main__":
    main(argv[1:])
