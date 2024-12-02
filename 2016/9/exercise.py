import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init


@timer
@print_result
def exercise1(arr):
    idx = 0
    parsed = []
    while idx < len(arr):
        if arr[idx] == "(":
            sub_ind = arr[idx:].index(")")
            marker = arr[idx + 1 : idx + sub_ind]

            l = int(marker.split("x")[0])
            rep = int(marker.split("x")[1])
            rest = arr[idx + len(marker) + 2 :]

            part = rest[:l]
            for _ in range(rep):
                parsed.append(part)

            idx += len(marker) + 1 + l

        else:
            parsed.append(arr[idx])
        idx += 1
    return len("".join(parsed))


@timer
@print_result
def exercise2(arr):
    idx = 0
    total_length = 0

    # returns length added
    def parse_rec(s):
        if len(s) == 0:
            return 0
        if s[0] != "(":
            return 1 + parse_rec(s[1:])

        idx = s.index(")")
        marker = s[1:idx]

        l = int(marker.split("x")[0])
        rep = int(marker.split("x")[1])

        section = s[idx + 1 :][:l]
        rest = s[idx + 1 + l :]

        return rep * parse_rec(section) + parse_rec(rest)

    return parse_rec(arr)


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    exercise1(arr[0])
    exercise2(arr[0])


if __name__ == "__main__":
    main(argv[1:])
