import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from itertools import chain, combinations, product


def battle(php, pdam, pdef, bhp, bdam, bdef):
    def dmg(damage, armor):
        return max(1, damage - armor)

    turn = 0
    while php > 0 and bhp > 0:
        if turn % 2 == 0:
            bhp -= dmg(pdam, bdef)
        else:
            php -= dmg(bdam, pdef)
        turn += 1
    return turn % 2 == 1


def created_combos():
    weapons = [[8, 4, 0], [10, 5, 0], [25, 6, 0], [40, 7, 0], [74, 8, 0]]
    armor = [[13, 0, 1], [31, 0, 2], [53, 0, 3], [75, 0, 4], [102, 0, 5]]
    rings = [[25, 1, 0], [50, 2, 0], [100, 3, 0], [20, 0, 1], [40, 0, 2], [80, 0, 3]]

    comb_a = weapons
    comb_b = list(chain.from_iterable(combinations(armor, r) for r in range(2)))
    comb_c = list(chain.from_iterable(combinations(rings, r) for r in range(3)))

    combos = [(a, *b, *c) for a in comb_a for b in comb_b for c in comb_c]

    summed_combos = [tuple(sum(values) for values in zip(*combo)) for combo in combos]
    return summed_combos


@timer
@print_result
def exercise1(arr):
    summed_combos = created_combos()
    summed_combos.sort(key=lambda x: x[0])
    for cost, damage, defence in summed_combos:
        if battle(100, damage, defence, 103, 9, 2):
            return cost


@timer
@print_result
def exercise2(arr):
    summed_combos = created_combos()
    summed_combos.sort(key=lambda x: x[0], reverse=True)
    for cost, damage, defence in summed_combos:
        if not battle(100, damage, defence, 103, 9, 2):
            return cost


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    exercise1(arr.copy())
    exercise2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
