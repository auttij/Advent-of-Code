from sys import argv
from os import path
from aocHelpers.decorators import aoc_part
from aocHelpers.init import init
from collections import deque
import z3


def bfs(target, buttons):
    q = deque()
    start = tuple("." for i in range(len(target)))
    q.append((start, 0))
    seen = set()

    while q:
        ls, clicks = q.popleft()
        if ls == target:
            return clicks
        if ls in seen:
            continue
        seen.add(ls)

        for b in buttons:
            q.append((tuple(switch(ls, b)), clicks + 1))
    return float("inf")


def switch(lights, buttons):
    new = {"#": ".", ".": "#"}
    return [new[val] if i in buttons else val for i, val in enumerate(lights[::])]


@aoc_part
def part1(data):
    total = 0
    for machine in data:
        target = tuple(machine[0])
        buttons = [set(map(int, btn.split(","))) for btn in machine[1:-1]]
        out = bfs(target, buttons)
        total += out
    return total


@aoc_part
def part2(data):
    total = 0
    for machine in data:
        s = z3.Optimize()
        joltages = list(map(int, machine[-1].split(",")))
        buttons = [set(map(int, btn.split(","))) for btn in machine[1:-1]]
        presses = [z3.Int(f"press{i}") for i in range(len(buttons))]

        for i in range(len(buttons)):
            s.add(presses[i] >= 0)
        for i in range(len(joltages)):
            s.add(
                sum(presses[j] for j, btn in enumerate(buttons) if i in btn)
                == joltages[i]
            )

        s.minimize(sum(presses))
        assert s.check() == z3.sat

        m = s.model()
        for b in presses:
            total += m[b].as_long()

    return total


def parse_input(raw):
    return [list(map(lambda x: x[1:-1], i.split())) for i in raw.splitlines()]


def main(args=None):
    raw = init(path.dirname(__file__), args)

    data1 = parse_input(raw)
    part1(data1)

    data2 = parse_input(raw)
    part2(data2)


if __name__ == "__main__":
    main(argv[1:])
