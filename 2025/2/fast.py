from sys import argv
from os import path
from aocHelpers.decorators import aoc_part, benchmark
from aocHelpers.init import init


@aoc_part
def part1(data):
    def next_invalid(a, b):
        start = int(a)
        end = int(b)

        len_a = len(a)
        len_b = len(b)

        # Canonicalize: if lengths differ or odd, jump to next even boundary
        if len_a % 2 != 0:
            # smallest even-length number with same digit count as a
            start = 10 ** (len_a - 1)
            len_a += 1
        if len_b % 2 != 0:
            # reduce upper bound to even length
            end = 10**len_b - 1
            len_b -= 1
        # now both have even lengths

        target_len = len_a
        while target_len <= len_b:
            half_len = target_len // 2
            half_start = 10 ** (half_len - 1)

            # Construct first candidate >= start
            n = half_start
            candidate = n * (10**half_len) + n

            if candidate < start:
                n = start // (10**half_len)
                candidate = n * (10**half_len) + n
                if candidate < start:
                    n += 1
                    candidate = n * (10**half_len) + n

            # Yield all in range
            while candidate <= end:
                yield candidate
                n += 1
                candidate = n * (10**half_len) + n

            target_len += 2

    sum = 0
    for a, b in data:
        for value in next_invalid(a, b):
            sum += value
    return sum


@aoc_part
def part2(data):
    def next_invalid(a, b):
        seen = set()
        start = int(a)
        end = int(b)

        for block_len in range(1, len(b) // 2 + 1):
            divisible_a = not len(a) % block_len
            divisible_b = not len(b) % block_len

            possible_multis = set()
            if divisible_a and len(a) != block_len:
                possible_multis.add(len(a) // block_len)
            if divisible_b and len(b) != block_len:
                possible_multis.add(len(b) // block_len)
            if not possible_multis:
                continue

            for mul in list(possible_multis):
                base = 10 ** (block_len - 1)
                candidate = int(str(base) * mul)

                while candidate < start:
                    base += 1
                    candidate = int(str(base) * mul)

                while candidate <= end:
                    if not candidate in seen:
                        yield candidate
                        seen.add(candidate)
                    base += 1
                    candidate = int(str(base) * mul)

    sum = 0
    for a, b in data:
        for value in next_invalid(a, b):
            sum += value
    return sum


def parse_input(raw):
    return [list(pair.split("-")) for pair in raw.split(",")]


def main(args=None):
    raw = init(path.dirname(__file__), args)

    data1 = parse_input(raw)
    part1(data1)

    data2 = parse_input(raw)
    part2(data2)


if __name__ == "__main__":
    main(argv[1:])
