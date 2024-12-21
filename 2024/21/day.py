from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from functools import lru_cache
from itertools import pairwise


numpad = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [None, "0", "A"],
]
dirpad = [[None, "^", "A"], ["<", "v", ">"]]
dirs = {">": (0, 1), "v": (1, 0), "<": (0, -1), "^": (-1, 0)}


def find_pos(grid, symbol):
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val == symbol:
                return (y, x)


@lru_cache
def shortest(start, end, layers):
    if start == "<" and end == ">":
        pass
    if layers == 0:
        return 1
    numpad_layer = True
    if isinstance(start, str):
        start = find_pos(dirpad, start)
        end = find_pos(dirpad, end)
        numpad_layer = False
    sy, sx = start
    ey, ex = end
    nl = layers - 1

    vert = "^" if ey < sy else "v" if ey > sy else None
    hori = "<" if ex < sx else ">" if ex > sx else None

    if vert:
        a_to_vert = shortest("A", vert, nl)
        vert_dist = (abs(ey - sy) - 1) * shortest(vert, vert, nl)
        vert_to_a = shortest(vert, "A", nl)
    if hori:
        a_to_hori = shortest("A", hori, nl)
        hori_dist = (abs(ex - sx) - 1) * shortest(hori, hori, nl)
        hori_to_a = shortest(hori, "A", nl)

    if not hori and not vert:
        return shortest("A", "A", nl)
    elif not hori:
        return a_to_vert + vert_dist + vert_to_a
    elif not vert:
        return a_to_hori + hori_dist + hori_to_a

    # fastest to press all of one direction, and then all of other direction
    hori_first = (
        a_to_hori + hori_dist + shortest(hori, vert, nl) + vert_dist + vert_to_a
    )
    vert_first = (
        a_to_vert + vert_dist + shortest(vert, hori, nl) + hori_dist + hori_to_a
    )

    if not numpad_layer:
        # avoid empty spot in dirpad
        if sx == 0:
            return hori_first
        elif ex == 0:
            return vert_first
        else:
            return min(hori_first, vert_first)
    else:
        # avoid empty spot in numpad
        if sx == 0 and ey == 3:
            return hori_first
        elif ex == 0 and sy == 3:
            return vert_first
        else:
            return min(hori_first, vert_first)


def solve(codes, layers):
    score = 0
    for code in codes:
        total = 0
        for start, end in pairwise("A" + code):
            total += shortest(find_pos(numpad, start), find_pos(numpad, end), layers)
        score += int(code[:-1]) * total
    return score


@timer
@print_result
def part1(arr):
    return solve(arr, 3)


@timer
@print_result
def part2(arr):
    return solve(arr, 26)


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    part1(arr.copy())
    part2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
