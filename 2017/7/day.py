from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from collections import Counter


def parse(arr):
    parsed = []
    for line in arr:
        parts = line.split()
        name = parts[0]
        weight = parts[1][1:-1]
        above = []
        for part in parts[3:]:
            if "," in part:
                above.append(part[:-1])
            else:
                above.append(part)
        parsed.append((name, weight, above))
    return parsed


def form_trees(arr):

    parent = {}
    children = {}
    weights = {}
    for line in arr:
        name, weight, above = line
        weights[name] = int(weight)
        if name not in parent:
            parent[name] = name
        for part in above:
            parent[part] = name
        children[name] = above
    return parent, children, weights


@timer
@print_result
def part1(arr):
    parent, _, _ = form_trees(arr)
    key = arr[0][0]
    while not key == parent[key]:
        key = parent[key]
    return key


@timer
@print_result
def part2(arr):
    parent, children, weights = form_trees(arr)

    root = arr[0][0]
    while not root == parent[root]:
        root = parent[root]

    def calculate_weight(node):
        node_weight = weights[node]
        child_weights = sum([calculate_weight(i) for i in children[node]])
        return node_weight + child_weights

    def is_balanced(node):
        if len(children[node]) == 0:
            return True

        child_weights = [calculate_weight(i) for i in children[node]]
        return min(child_weights) == max(child_weights)

    def find_unbalance(node, target=None):
        child_count = len(children[node])

        if child_count == 0:
            print(node)
        if child_count > 2:
            child_weights = {i: calculate_weight(i) for i in children[node]}
            c = Counter(child_weights.values())
            target = c.most_common(1)[0][0]
            odd_amount = min(c, key=c.get)
            odd = [k for k, v in child_weights.items() if v == odd_amount][0]
            return find_unbalance(odd, target)
        elif child_count == 2:
            balanced_children = [is_balanced(child) for child in children[node]]
            if all(balanced_children):
                return target - sum([calculate_weight(i) for i in children[node]])
        pass

    return find_unbalance(root)

    print(calculate_weight(root))


def main(args=None):
    orig = init(path.dirname(__file__), inputs.read_to_str_arr, args)
    arr = parse(orig)
    part1(arr.copy())
    part2(arr.copy())


if __name__ == "__main__":
    main(argv[1:])
