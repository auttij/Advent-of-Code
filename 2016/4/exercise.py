import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from collections import Counter


def parse(line):
    parts = line.split("[")
    return parts[0], parts[1][:-1]


def common_letters(name):
    only_letters = "".join(name.split("-"))
    c = Counter(only_letters)
    sorted_letters = sorted(c.items(), key=lambda x: (-x[1], x[0]))
    top_five = [letter for letter, count in sorted_letters[:5]]
    return "".join(top_five)


@timer
@print_result
def exercise1(arr):
    valid = 0
    for line in arr:
        full_name, checksum = parse(line)
        name = full_name[:-4]
        sector_id = int(full_name[-3:])
        common = common_letters(name)

        if common == checksum:
            valid += sector_id
    return valid
    # print(name, checksum)


def alphabet_shift(letter, count):
    if letter == "-":
        return " "
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    idx = (alphabet.index(letter) + count) % len(alphabet)
    return alphabet[idx]


@timer
@print_result
def exercise2(arr):
    for line in arr:
        full_name, checksum = parse(line)
        name = full_name[:-4]
        sector_id = int(full_name[-3:])
        common = common_letters(name)

        if common != checksum:
            continue

        word = "".join(map(lambda x: alphabet_shift(x, sector_id), name))
        if "north" in word:
            return sector_id


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    exercise1(arr.copy())
    exercise2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
