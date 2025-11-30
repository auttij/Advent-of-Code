from aocHelpers.testing import TestCase, run_tests
from day import part1, part2, parse_input


def read_data(filename):
    with open(filename) as f:
        return f.read()


input1 = parse_input(read_data("input1.txt"))


cases = [
    TestCase("part 1 example", input1, 12),
]

run_tests(part1, cases)


input3 = parse_input(read_data("input3.txt"))

cases = [
    TestCase("part 2 example", input3, "fgij"),
]

run_tests(part2, cases)
