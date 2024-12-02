import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from aocHelpers.helpers import transpose

def expand_rows(input):
	out = []
	for line in input:
		if not '#' in set(line):
			out.append(['E'] * len(line))
		else:		
			out.append(line)
	return out

def expand(input):
	mid = transpose(expand_rows(input))
	return transpose(expand_rows(mid))

def dist(pos1, pos2):
	return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def get_positions(input, factor):
	pos = []
	ye = 0 # amount of expanded rows
	# calculate positions with expansion
	for y, row in enumerate(input):
		s = set(row)
		if len(s) == 1 and 'E' in s:
			ye += 1
			continue

		xe = 0 # amount of expanded columns
		for x, c in enumerate(row):
			if c == 'E':
				xe += 1
			if c == "#":
				y_val = y + factor * ye
				x_val = x + factor * xe
				pos.append((y_val, x_val))
	return pos

def calculate(input, factor):
	expanded = expand(input)
	pos = get_positions(expanded, factor - 1)

	total_distance = 0
	for i, p1 in enumerate(pos):
		for p2 in pos[i+1:]:
			total_distance += dist(p1, p2)
	return total_distance

@timer
@print_result
def part1(input):
	return calculate(input, 2)

@timer
@print_result
def part2(input):
	return calculate(input, 1_000_000)

def main(args=None):
	input = init(path.dirname(__file__), inputs.read_to_str_arr, args)
	part1(input.copy())
	part2(input.copy())

if __name__ == "__main__":
	main(argv[1:])
