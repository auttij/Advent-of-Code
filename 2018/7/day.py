from sys import argv
from os import path
from aocHelpers.decorators import aoc_part
from aocHelpers.init import init


def get_prev_next(instructions):

    prev = {}
    nxt = {}
    for pre, post in instructions:
        if pre not in prev:
            prev[pre] = []
            nxt[pre] = []
        if post not in prev:
            prev[post] = []
            nxt[post] = []
        prev[post].append(pre)
        nxt[pre].append(post)
    return prev, nxt


@aoc_part
def part1(arr):
    prev, nxt = get_prev_next(arr)

    out = []
    while len(out) < len(prev.keys()):
        ready = [k for k, v in prev.items() if len(v) == 0 and k not in out]
        candidate = sorted(ready)[0]

        out.append(candidate)
        conditionals = nxt[candidate]
        for value in conditionals:
            prev[value].remove(candidate)

    return "".join(out)


@aoc_part
def part2(arr):
    prev, nxt = get_prev_next(arr)

    workers = 5
    elapsed_time = 0
    work_times = [0] * workers
    work_chars = [None] * workers
    handled = []

    while len(handled) < len(prev.keys()):
        ready = [
            k
            for k, v in prev.items()
            if len(v) == 0 and k not in handled and k not in work_chars
        ]
        empty = work_times.count(0)

        for i in range(min(empty, len(ready))):
            ind = work_times.index(0)
            work_times[ind] = 61 + ord(ready[i]) - ord("A")
            work_chars[ind] = ready[i]

        # elapse time
        smallest = min(i for i in work_times if i != 0)
        elapsed_time += smallest
        work_times = [max(0, i - smallest) for i in work_times]
        handle = []
        for i, c in enumerate(work_chars):
            if c != None and work_times[i] == 0:
                handle.append(c)
                work_chars[i] = None

        for candidate in handle:
            conditionals = nxt[candidate]
            for value in conditionals:
                if candidate in prev[value]:
                    prev[value].remove(candidate)
            handled.append(candidate)
    return elapsed_time


def parse_input(raw):
    # arr
    # return raw.splitlines()

    # int arr
    # return list(map(int, raw.splitlines()))

    # str pairs
    asd = [line.split(" ") for line in raw.splitlines()]
    return [(i[1], i[-3]) for i in asd]

    # select numbers from input
    # import re
    # return [tuple(map(int, re.findall(r"-?\d+", line))) for line in raw.splitlines()]

    return raw


def main(args=None):
    raw = init(path.dirname(__file__), args)

    data1 = parse_input(raw)
    part1(data1)

    data2 = parse_input(raw)
    part2(data2)


if __name__ == "__main__":
    main(argv[1:])
