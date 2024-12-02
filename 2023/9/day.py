import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init

def extrapolate(input):
	## generate history
	histories = [input]
	while histories[-1] != [0] * len(histories[-1]):
		top = histories[-1]
		histories.append([top[i + 1] - e for i, e in enumerate(top[:-1])])

	# extrapolate each history
	histories[-1].append(0)
	for i, h in enumerate(histories[::-1][1:]):
		h.append(h[-1] + histories[::-1][i][-1])
	return histories[0][-1]

@timer
@print_result
def part1(input):
	return sum((extrapolate(list(i)) for i in input))

@timer
@print_result
def part2(input):
	return sum((extrapolate(list(i[::-1])) for i in input))

def main(args=None):
	input = init(path.dirname(__file__), inputs.read_to_int_tuple_arr, args)
	if isinstance(input, str):
		part1(input)
		part2(input)
	else:
		part1(input.copy())
		part2(input.copy())

if __name__ == "__main__":
	main(argv[1:])
