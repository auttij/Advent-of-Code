import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from functools import reduce
from itertools import combinations
from math import ceil


def QE(l):
    return reduce(lambda x, y: x * y, l)


def can_partition(l, target, group1, group2):
    if sum(group1) == sum(group2) == target:
        return group1, group2

    if not l:
        return None

    current = l[0]
    rest = l[1:]

    solution = can_partition(rest, target, group1 + [current], group2)
    if solution:
        return solution

    solution2 = can_partition(rest, target, group1, group2 + [current])
    if solution2:
        return solution2


def split_list_two(l, target):
    result = can_partition(l, target, [], [])
    if result:
        return result
    else:
        return None


@timer
@print_result
def exercise1(arr):
    total = sum(arr)
    third = total // 3

    print(total, third)

    for length in range(2, ceil(len(arr) / 3) + 1):
        print(f"checking {length = }")
        min_qe = 9999999999999999
        solution = []

        combos = [i for i in combinations(arr, length) if sum(i) == third]
        print(f"{len(combos)} combinations")
        for combination in combos:
            rest = [i for i in arr if i not in combination]
            if split_list_two(rest, third):
                qe = QE(combination)
                if qe < min_qe:
                    min_qe = qe
                    solution = combination

        if solution:
            return min_qe


def can_partition3(l, target, group1, group2, group3):
    if sum(group1) == sum(group2) == sum(group3) == target:
        return group1, group2, group3
    if not l:
        return None
    if sum(group1) > target or sum(group2) > target or sum(group3) > target:
        return None

    current = l[0]
    rest = l[1:]

    solution = can_partition3(rest, target, group1 + [current], group2, group3)
    if solution:
        return solution

    solution2 = can_partition3(rest, target, group1, group2 + [current], group3)
    if solution2:
        return solution2

    solution3 = can_partition3(rest, target, group1, group2, group3 + [current])
    if solution3:
        return solution3


def split_list_three(l, target):
    result = can_partition3(l, target, [], [], [])
    if result:
        return result
    else:
        return None


@timer
@print_result
def exercise2(arr):
    total = sum(arr)
    quart = total // 4

    print(total, quart)

    for length in range(2, ceil(len(arr) / 3) + 1):
        print(f"checking {length = }")
        min_qe = 999999999999999999
        solution = []

        combos = [i for i in combinations(arr, length) if sum(i) == quart]
        print(f"{len(combos)} combinations")
        for combination in combos:
            rest = [i for i in arr if i not in combination]
            if split_list_three(rest, quart):
                qe = QE(combination)
                if qe < min_qe:
                    min_qe = qe
                    solution = combination

        if solution:
            return min_qe


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_int_arr, args)
    exercise1(arr.copy())
    exercise2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
