from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from collections import deque


@timer
@print_result
def part1(arr):
    out = []
    num = 0
    for i, char in enumerate(arr):
        if i % 2 == 0:
            for _ in range(int(char)):
                out.append(num)
            num += 1
        else:
            for _ in range(int(char)):
                out.append(".")

    w = len(out) - 1
    i = 0
    j = w
    while i < j:
        while i < w and out[i] != ".":
            i += 1
        while j > 0 and out[j] == ".":
            j -= 1
        if out[i] == "." and out[j] != ".":
            out[i], out[j] = out[j], out[i]
    out[i], out[j] = out[j], out[i]
    s = 0
    for i, char in enumerate(out):
        if char == ".":
            break
        s += i * int(char)
    return s


def solve(arr):
    DATA = deque([])
    SPACE = deque([])
    FINAL = []

    file_id = 0
    pos = 0
    for i, c in enumerate(arr):
        if i % 2 == 0:
            DATA.append((pos, int(c), file_id))
            for i in range(int(c)):
                FINAL.append(file_id)
                pos += 1
            file_id += 1
        else:
            SPACE.append((pos, int(c)))
            for i in range(int(c)):
                FINAL.append(None)
                pos += 1

    for pos, size, file_id in reversed(DATA):
        for space_i, (space_pos, space_size) in enumerate(SPACE):
            if space_pos < pos and size <= space_size:
                for i in range(size):
                    FINAL[pos + i] = None
                    FINAL[space_pos + i] = file_id
                SPACE[space_i] = (space_pos + size, space_size - size)
                break
    return FINAL


@timer
@print_result
def part2(arr):
    result = solve(arr)
    s = 0
    for i, num in enumerate(result):
        if num:
            s += i * num
    return s


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str, args)
    part1(arr)
    part2(arr)


if __name__ == "__main__":
    main(argv[1:])
