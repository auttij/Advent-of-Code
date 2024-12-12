from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from aocHelpers.helpers import adjacent


moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def num_sides(grp):
    sseen = set()
    ccs = 0
    for y, x in grp:
        for dy, dx in moves:
            if (y + dy, x + dx) in grp:
                continue
            # n = outside, d = outside "side"
            # find 'canonical' corner side
            cy, cx = y, x
            while (cy + dx, cx + dy) in grp and (cy + dy, cx + dx) not in grp:
                cy += dx
                cx += dy
            if (cy, cx, dy, dx) not in sseen:
                sseen.add((cy, cx, dy, dx))
                ccs += 1
    return ccs


def get_values(arr):
    vals = {}
    for y, row in enumerate(arr):
        for x, val in enumerate(row):
            if val not in vals:
                vals[val] = []
            vals[val].append((y, x))
    return vals


def create_groups(vals, arr):
    h, w = len(arr), len(arr[0])
    groups = {}
    for k, poses in vals.items():
        out = []

        remaining = poses
        group_i = 0
        while remaining:
            stack = [remaining.pop(0)]
            i = 0
            while i < len(stack):
                for p in adjacent(stack[i]):
                    yp, xp = p
                    if 0 <= yp < h and 0 <= xp < w:
                        if arr[yp][xp] == k and p not in stack:
                            stack.append(p)
                i += 1
            out.append(stack)
            flat_out = [x for y in out for x in y]
            remaining = [a for a in remaining if a not in flat_out]
            group_i += 1

        groups[k] = out
    return groups


@timer
@print_result
def part1(arr):
    vals = get_values(arr)
    groups = create_groups(vals, arr)

    s = 0
    for key, gs in groups.items():
        for group in gs:
            perimeter = 0
            for pos in group:
                for p in adjacent(pos):
                    yp, xp = p
                    if 0 <= yp < len(arr) and 0 <= xp < len(arr[0]):
                        if arr[yp][xp] != key:
                            perimeter += 1
                    else:
                        perimeter += 1
            s += perimeter * len(group)
    return s


@timer
@print_result
def part2(arr):
    vals = get_values(arr)
    groups = create_groups(vals, arr)

    s = 0
    for key, gs in groups.items():
        for group in gs:
            sides = num_sides(group)
            s += len(group) * sides
    return s


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    part1(arr.copy())
    part2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
