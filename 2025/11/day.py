from sys import argv
from os import path
from aocHelpers.decorators import aoc_part
from aocHelpers.init import init
from functools import lru_cache


def count_routes(graph, start, end):
    def dfs(node):
        if node == end:
            return 1

        total = 0
        for nxt in graph[node]:
            total += dfs(nxt)
        return total

    return dfs(start)


@aoc_part
def part1(data):
    graph = {i[0]: i[1:] for i in data}
    return count_routes(graph, "you", "out")


def count_routes_with_flags(graph, start, end):
    @lru_cache(None)
    def dfs(node, seen_fft, seen_dac):
        if node == "fft":
            seen_fft = True
        if node == "dac":
            seen_dac = True

        if node == end:
            return 1 if (seen_fft and seen_dac) else 0

        total = 0
        for nxt in graph[node]:
            total += dfs(nxt, seen_fft, seen_dac)
        return total

    return dfs(start, False, False)


@aoc_part
def part2(data):
    graph = {i[0]: i[1:] for i in data}
    return count_routes_with_flags(graph, "svr", "out")


def parse_input(raw):
    return [list(map(lambda x: x[:3], i.split())) for i in raw.splitlines()]


def main(args=None):
    raw = init(path.dirname(__file__), args)

    data1 = parse_input(raw)
    part1(data1)

    data2 = parse_input(raw)
    part2(data2)


if __name__ == "__main__":
    main(argv[1:])
