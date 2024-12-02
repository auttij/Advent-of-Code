import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
import re

@timer
@print_result
def part1(input):
	out = 0
	for line in input:
		win_str, mine_str = line.split('|')
		winning = [int(x) for x in win_str.split(":")[1].split()]
		mine = [int(x) for x in mine_str.split()]
		mine = [x for x in mine if x in winning]
		if len(mine):
			out += 2**(len(mine)-1)
	return out


@timer
@print_result
def part2(input):
	out = 0
	multipliers = [1 for _ in input]

	for i, line in enumerate(input):
		win_str, mine_str = line.split('|')
		winning = [int(x) for x in win_str.split(":")[1].split()]
		mine = [int(x) for x in mine_str.split()]
		mine = [x for x in mine if x in winning]

		multi = multipliers[i]
		for j in range(i + 1, min(i + len(mine) + 1, len(input))):
			multipliers[j] += multi
		out += multi
	return out


def main(args=None):
	input = init(path.dirname(__file__), inputs.read_to_str_arr, args)
	if isinstance(input, str):
		part1(input)
		part2(input)
	else:
		part1(input.copy())
		part2(input.copy())

if __name__ == "__main__":
	main(argv[1:])
