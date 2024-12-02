import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init


@timer
@print_result
def exercise1(n):
    power_of_2 = 1
    while power_of_2 * 2 <= n:
        power_of_2 *= 2

    # Calculate the survivor's position
    survivor = 2 * (n - power_of_2) + 1
    return survivor

    # elves = [i for i in range(1, count + 1)]
    # while len(elves) > 1:
    #     elves = [v for i, v in enumerate(elves) if i % 2 == 0][len(elves) % 2 :]
    # return elves[0]


@timer
@print_result
def exercise2(n):
    # elves = [i for i in range(1, n + 1)]
    # idx = 0
    # n = len(elves)
    # while n > 1:
    #     removed = elves.pop((idx + n // 2) % n)
    #     print(removed)
    #     idx = (idx + 1) % n
    #     n -= 1
    # return elves[0]

    power_of_3 = 1
    while power_of_3 * 3 <= n:
        power_of_3 *= 3

    # Calculate the position of the last elf
    if n == power_of_3:
        return 1  # Special case where n is a power of 3
    else:
        return n - power_of_3 + max(n - 2 * power_of_3, 0)


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_int_arr, args)
    exercise1(arr[0])
    exercise2(arr[0])


if __name__ == "__main__":
    main(argv[1:])
