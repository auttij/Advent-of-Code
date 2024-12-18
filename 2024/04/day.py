from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init


def search(arr, pos, target):
    y, x = pos
    found = 0
    for yi in range(-1, 2):
        for xi in range(-1, 2):
            new_pos = [(y + yi * i, x + xi * i) for i in range(1, 4)]
            letters = [
                arr[ys][xs]
                for ys, xs in new_pos
                if 0 <= ys < len(arr) and 0 <= xs < len(arr[0])
            ]
            if "".join(letters) == target[-3:]:
                found += 1
    return found


@timer
@print_result
def part1(arr):
    target = "XMAS"
    found = 0
    for y, row in enumerate(arr):
        for x, val in enumerate(row):
            if val == target[0]:
                found += search(arr, (y, x), target)
    return found


def search2(arr, pos):
    def to_pos(coord):
        ys, xs = coord
        return arr[ys][xs]

    y, x = pos
    vals1 = "".join(map(to_pos, [(y - 1, x - 1), (y + 1, x + 1)]))
    vals2 = "".join(map(to_pos, [(y + 1, x - 1), (y - 1, x + 1)]))
    return vals1 in ["MS", "SM"] and vals2 in ["MS", "SM"]


@timer
@print_result
def part2(arr):
    found = 0
    for y, row in enumerate(arr[1:-1], start=1):
        found += sum(
            [
                search2(arr, (y, x))
                for x, val in enumerate(row[1:-1], start=1)
                if val == "A"
            ]
        )
    return found


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    part1(arr.copy())
    part2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
