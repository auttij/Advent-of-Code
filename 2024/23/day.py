from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from itertools import combinations


def parse(arr):
    global neighbors
    neighbors = {}
    pairs = [tuple(i.split("-")) for i in arr]
    for a, b in pairs:
        if a not in neighbors:
            neighbors[a] = []
        neighbors[a].append(b)
        if b not in neighbors:
            neighbors[b] = []
        neighbors[b].append(a)


@timer
@print_result
def part1():
    candidates = [node for node in neighbors.keys() if node[0] == "t"]
    triplets = set()

    for a in candidates:
        n_a = neighbors[a]
        for b in n_a:
            n_b = neighbors[b]
            for c in n_b:
                if c in n_a:
                    triplets.add(tuple(sorted((a, b, c))))
    return len(triplets)


def is_clique(nodes):
    return all(
        node in neighbors[other] for node in nodes for other in nodes if node != other
    )


def find_largest_clique():
    candidates = [node for node in neighbors.keys() if node[0] == "t"]
    largest_clique = []

    for node in candidates:
        n_a = neighbors[node]
        for sub in range(1, len(n_a) + 1):
            for combo in combinations(n_a, sub):
                clique = (node,) + combo
                if is_clique(clique) and len(clique) > len(largest_clique):
                    largest_clique = list(clique)
    return largest_clique


def find_largest_clique_fast():
    candidates = [node for node in neighbors.keys() if node[0] == "t"]
    largest_clique = ()

    seen = set()

    for node in candidates:
        if node in seen:
            continue

        n_a = neighbors[node]
        sub = len(n_a)

        while sub >= len(largest_clique):
            for combo in combinations(n_a, sub):
                clique = (node,) + combo
                if is_clique(clique) and len(clique) > len(largest_clique):
                    largest_clique = clique
                    seen.update(clique)
                    break
            sub -= 1
    return largest_clique


@timer
@print_result
def part2():
    return ",".join(sorted(find_largest_clique_fast()))


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    parse(arr)
    part1()
    part2()


if __name__ == "__main__":
    main(argv[1:])
