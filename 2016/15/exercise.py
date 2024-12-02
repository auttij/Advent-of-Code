import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from aocHelpers.helpers import chinese_remainder_theorem


@timer
@print_result
def exercise1(arr):
    # starting position pi, number of positions ni
    # discs will be at position 0 after t seconds if:
    # (t + i + pi) (mod ni) = 0
    # => t = -i - pi (mod ni)

    discs = [(pos, count) for _, count, _, pos in arr]
    positions, modulos = list(zip(*discs))
    target_positions = [
        (-positions[i] - i - 1) % modulos[i] for i in range(len(modulos))
    ]
    return chinese_remainder_theorem(modulos, target_positions)


@timer
@print_result
def exercise2(arr):
    discs = [(pos, count) for _, count, _, pos in arr]
    discs.append((0, 11))

    positions, modulos = list(zip(*discs))
    target_positions = [
        (-positions[i] - i - 1) % modulos[i] for i in range(len(modulos))
    ]
    return chinese_remainder_theorem(modulos, target_positions)


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_int_tuple_arr, args)
    exercise1(arr.copy())
    exercise2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
