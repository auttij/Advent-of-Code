import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
import re
from statistics import mean
from math import ceil


def parse(arr):
    last = arr[-1].split(" ")[0].split("-")
    xm, ym = int(last[-2][1:]) + 1, int(last[-1][1:]) + 1
    parsed = [[(nx, ny) for nx in range(xm)] for ny in range(ym)]
    for i, line in enumerate(arr[2:]):
        x = i // ym
        y = i % ym
        splt = re.sub(" +", " ", line).split(" ")
        _, size, used, avail, _ = splt
        parsed[y][x] = (int(size[:-1]), int(used[:-1]), int(avail[:-1]))
    return parsed


def check_viable(a, b):
    viable = a[1] > 0 and a[1] < b[2]
    return 1 if viable else 0


@timer
@print_result
def exercise1(nodes):
    viable = 0
    for y1 in range(len(nodes)):
        for x1 in range(len(nodes[0])):
            for y2 in range(len(nodes)):
                for x2 in range(len(nodes[0])):
                    if x1 == x2 and y1 == y2:
                        continue
                    a = nodes[y1][x1]
                    b = nodes[y2][x2]
                    viable += check_viable(a, b)
    return viable


def pretty_print(nodes):
    print()
    for i, row in enumerate(nodes):
        row_str = " -- ".join([f"{used}T/{size}T" for size, used, _ in row])
        print(row_str)
        if i < len(nodes) - 1:
            print("     ".join(["   |" for i in range(len(row))]))
    print()


def simple_print(nodes, goal):
    avg = ceil(mean(list(map(lambda x: x[0], (x for y in nodes for x in y)))))
    for y, row in enumerate(nodes):
        line = []
        for x, node in enumerate(row):
            size, used, avail = node
            if (x, y) == goal:
                line.append("G")
            elif size > avg:
                line.append("#")
            elif used == 0:
                line.append("_")
            else:
                line.append(".")
        print(" ".join(line))


@timer
@print_result
def exercise2(nodes):
    goal = (0, 0)
    start = (len(nodes[0]) - 1, 0)
    empty = (0, 0)

    for y, row in enumerate(nodes):
        for x, node in enumerate(row):
            size, used, avail = node
            if used == 0:
                empty = (x, y)

    # print(start, empty)
    # pretty_print(nodes)
    simple_print(nodes, start)
    # answer was 227
    # pretty print and calculate path length manually :)
    pass


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    nodes = parse(arr)
    exercise1(nodes.copy())
    exercise2(nodes.copy())


if __name__ == "__main__":
    main(argv[1:])
