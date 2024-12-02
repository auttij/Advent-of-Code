import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from functools import reduce
from itertools import product


def parse(arr):
    out = []
    for line in arr:
        splt = line.split(" ")
        out.append(
            list(
                map(
                    int,
                    [splt[2][:-1], splt[4][:-1], splt[6][:-1], splt[8][:-1], splt[10]],
                )
            )
        )
    return out


def score(inputs, weights):
    out = []
    for i in range(4):
        score = sum(
            map(lambda x: x[0] * x[1], zip(map(lambda x: x[i], inputs), weights))
        )
        if score <= 0:
            return 0
        out.append(score)
    return reduce(lambda x, y: x * y, out)


@timer
@print_result
def exercise1(arr):
    input = list(map(lambda x: x[:-1], parse(arr)))

    # Define the range and total
    total = 100
    max_value = 100

    combination = []
    top = 0

    for x1 in range(max_value + 1):
        for x2 in range(max_value + 1 - x1):
            for x3 in range(max_value + 1 - x1 - x2):
                x4 = total - x1 - x2 - x3
                weights = [x1, x2, x3, x4]
                s = score(input, weights)
                if s > top:
                    top = s
                    combination = weights

    print(combination)
    return top


def calories(inputs, weights):
    cals = list(map(lambda x: x[-1], inputs))
    return sum(map(lambda x: x[0] * x[1], zip(cals, weights)))


@timer
@print_result
def exercise2(arr):
    input = parse(arr)

    # Define the range and total
    total = 100
    max_value = 100

    combination = []
    top = 0

    for x1 in range(max_value + 1):
        for x2 in range(max_value + 1 - x1):
            for x3 in range(max_value + 1 - x1 - x2):
                x4 = total - x1 - x2 - x3
                weights = [x1, x2, x3, x4]
                s = score(input, weights)
                if calories(input, weights) == 500:
                    if s > top:
                        top = s
                        combination = weights

    print(combination)
    return top


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    exercise1(arr.copy())
    exercise2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
