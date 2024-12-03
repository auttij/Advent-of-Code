from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init


@timer
@print_result
def part1(arr):
    seen = set()
    vals = list(arr)
    key = "".join(map(str, vals))

    while not key in seen:
        seen.add(key)
        m = max(vals)
        m_idx = vals.index(m)
        vals[m_idx] = 0

        for i in range(m):
            idx = (m_idx + 1 + i) % len(vals)
            vals[idx] += 1
        key = "".join(map(str, vals))
    return len(seen)


@timer
@print_result
def part2(arr):
    seen = {}
    vals = list(arr)
    key = "".join(map(str, vals))

    iter = 0
    while not key in seen:
        seen[key] = iter
        iter += 1
        m = max(vals)
        m_idx = vals.index(m)
        vals[m_idx] = 0

        for i in range(m):
            idx = (m_idx + 1 + i) % len(vals)
            vals[idx] += 1
        key = "".join(map(str, vals))

    print(iter, seen[key])
    return iter - seen[key]


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_int_tuple_arr, args)
    part1(arr.copy()[0])
    part2(arr.copy()[0])


if __name__ == "__main__":
    main(argv[1:])
