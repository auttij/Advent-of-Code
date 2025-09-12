from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init


def parse(line):
    ind, val = line.split(" <-> ")
    return int(ind), [int(x) for x in val.split(", ")]


def bfs(graph, start):
    seen = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node in seen:
            continue
        seen.add(node)
        for neighbor in graph[node]:
            if neighbor not in seen:
                queue.append(neighbor)
    return seen


@timer
@print_result
def part1(arr):
    parsed = [parse(line) for line in arr]
    graph = {ind: vals for ind, vals in parsed}

    group = bfs(graph, 0)
    return len(group)


@timer
@print_result
def part2(arr):
    parsed = [parse(line) for line in arr]
    graph = {ind: vals for ind, vals in parsed}

    groups = 0
    indices = set(graph.keys())
    while indices:
        start = indices.pop()
        group = bfs(graph, start)
        indices.difference_update(group)
        groups += 1
    return groups


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    part1(arr.copy())
    part2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
