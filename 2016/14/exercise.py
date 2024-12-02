import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from hashlib import md5
from collections import Counter


def x_in_a_rows(s, x, single=False):
    matches = set()
    for i in range(len(s) - (x - 1)):
        if len(set(s[i : i + x])) == 1:
            if single:
                return s[i]
            matches.add(s[i])

    if single:
        return None
    else:
        return matches


def hash(input):
    m = md5()
    m.update(input)
    return m.hexdigest()


def hash_with_salt(salt, idx):
    return hash(bytes(salt + str(idx), "utf8"))


def find_key_idx(salt, hash_function):
    fives_counter = Counter()
    for i in range(0, 1001):
        h = hash_function(salt, i)
        for match in x_in_a_rows(h, 5):
            fives_counter[match] += 1

    keys = 0
    idx = 0
    while True:
        h = hash_function(salt, idx)

        for five_match in x_in_a_rows(h, 5):
            fives_counter[five_match] -= 1
            fives_counter = Counter({k: c for k, c in fives_counter.items() if c > 0})

        three_match = x_in_a_rows(h, 3, single=True)
        if three_match in fives_counter.keys():
            keys += 1
            if keys == 64:
                return idx

        idx += 1

        new_hash = hash_function(salt, idx + 1000)
        for match in x_in_a_rows(new_hash, 5):
            fives_counter[match] += 1


@timer
@print_result
def exercise1(salt):
    return find_key_idx(salt, hash_with_salt)


def hash2(salt, idx):
    hash_input = salt + str(idx)
    for i in range(2017):
        hash_input = hash(bytes(hash_input, "utf8"))
    return hash_input


@timer
@print_result
def exercise2(salt):
    return find_key_idx(salt, hash2)


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    exercise1(arr[0])
    exercise2(arr[0])


if __name__ == "__main__":
    main(argv[1:])
