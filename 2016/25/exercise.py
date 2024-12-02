import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init

IDXS = ["a", "b", "c", "d"]


def process(vals, arr):
    cmd_idx = 0
    out = []
    while cmd_idx < len(arr):
        if len(out) == 10:
            return out
        line = arr[cmd_idx]
        splt = line.split(" ")
        if len(splt) == 2:
            splt.append(None)

        cmd, x, y = splt
        if x.isalpha():
            if cmd in ["cpy", "jnz"]:
                x = vals[IDXS.index(x)]
            else:
                x = IDXS.index(x)
        else:
            x = int(x)

        if y:
            if y.isalpha():
                y = IDXS.index(y)
            else:
                y = int(y)

        if cmd == "cpy":
            vals[y] = x
        if cmd == "inc":
            vals[x] += 1
        if cmd == "dec":
            vals[x] -= 1
        if cmd == "out":
            out.append(str(vals[x]))

        if cmd == "jnz" and x != 0:
            cmd_idx += y
        else:
            cmd_idx += 1
    return vals


@timer
@print_result
def exercise1(arr):
    for i in range(1000):
        vals = [i, 0, 0, 0]
        out = process(vals, arr)
        if "".join(out) == "0101010101":
            return i


@timer
@print_result
def exercise2(arr):
    vals = [0, 0, 1, 0]
    return process(vals, arr)[0]


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    exercise1(arr.copy())
    exercise2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
