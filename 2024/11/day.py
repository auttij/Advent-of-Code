from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from collections import Counter


def change_stone(stone):
    if stone == 0:
        return (1,)
    s = str(stone)
    if len(s) % 2 == 0:
        l = len(s)
        return int(s[: l // 2]), int(s[l // 2 :])
    return (stone * 2024,)


def count_stones(stones, rounds):
    c = Counter(stones)
    for _ in range(rounds):
        nc = Counter()
        for k, count in c.items():
            for stone in change_stone(k):
                nc[stone] += count
        c = nc
    return sum(c.values())


@timer
@print_result
def part1(arr):
    return count_stones(arr[0], 25)


@timer
@print_result
def part2(arr):
    return count_stones(arr[0], 75)


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_int_tuple_arr, args)
    part1(arr.copy())
    part2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
