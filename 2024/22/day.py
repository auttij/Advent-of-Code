from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init

MOD = 16777216


def calculate(secret, iterations=1):
    for _ in range(iterations):
        secret = (secret ^ (secret << 6)) % MOD
        secret = (secret >> 5) ^ secret
        secret = ((secret << 11) ^ secret) % MOD
    return secret


@timer
@print_result
def part1(arr):
    return sum(calculate(i, 2000) for i in arr)


def first_sequence_values(secret):
    seqs = {}
    seq = 0
    prev = secret % 10
    lim = 32767  # 2^15 - 1

    for _ in range(2000):
        secret = calculate(secret)
        val = secret % 10
        seq = ((lim & seq) << 5) + (val - prev + 9)
        seqs.setdefault(seq, val)
        prev = val
    return seqs


def calculate_best_sequence(arr):
    totals = {}
    for secret in arr:
        seqs = first_sequence_values(secret)
        for k, v in seqs.items():
            totals[k] = totals.get(k, 0) + v
    return max(totals.items(), key=lambda item: item[1])[1]


@timer
@print_result
def part2(arr):
    return calculate_best_sequence(arr)


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_int_arr, args)
    part1(arr.copy())
    part2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
