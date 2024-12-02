import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init

def tilt(input, dir):
	rocks = []
	for y, row in enumerate(input):
		for x, c in enumerate(row):
			if c == 'O':
				rocks.append((y, x))
	
	k = 0 if abs(dir[0]) > abs(dir[1]) else 1
	rev = dir[k] > 0
	rocks.sort(key=lambda x: x[k], reverse=rev)

	for (y, x) in rocks:
		cy, cx = y, x
		while True:
			np = (cy + dir[0], cx + dir[1])
			if np[0] < 0 or (len(input) - 1) < np[0] or (len(input) - 1) < np[1] or np[1] < 0:
				break
			elif input[np[0]][np[1]] == '.':
				input[np[0]][np[1]] = 'O'
				input[cy][cx] = '.'
			else:
				break
			cy = np[0]
			cx = np[1]
	return input


def load(input):
	ly = len(input)

	out = 0
	for y, row in enumerate(input):
		for x, c in enumerate(row):
			if c == 'O':
				out += ly - y
	return out


@timer
@print_result
def part1(input):
	g = [list(l) for l in input]

	north = (-1, 0)
	tilted = tilt(g, north)
	return load(tilted)


def to_key(input):
	return "".join(["".join(l) for l in input])


@timer
@print_result
def part2(input):
	g = [list(l) for l in input]
	
	north = (-1, 0)
	south = (1, 0)
	west = (0, -1)
	east = (0, 1)
	cycle = [north, west, south, east]

	cur = g
	fp = {}
	cycles = 0
	
	while True:
		for c in cycle:
			cur = tilt(cur, c)
		cycles += 1
		k = to_key(cur)
		if k not in fp:
			fp[k] = cycles
		else:
			break

	# How many cycles until it starts repeating
	cyc_len = cycles - fp[k]
	total = 1000000000

	# skip until almost the end
	skip = (total - cycles) // cyc_len
	skipped = cycles + (skip * cyc_len)

	# iterate until end
	while skipped < total:
		for c in cycle:
			cur = tilt(cur, c)
		skipped += 1

	return load(cur)



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
