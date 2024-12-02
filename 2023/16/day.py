import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init


north = (-1, 0)
south = (1, 0)
west = (0, -1)
east = (0, 1)
dirs = [east, south, west, north]
transform = {
	(0,"\\"): 1,
	(0,"/"): 3,
	(0,"|"): [1, 3],
	(0, "-"): 0,
	(1,"\\"): 0,
	(1,"/"): 2,
	(1,"|"): 1,
	(1, "-"): [0, 2],
	(2,"\\"): 3,
	(2,"/"): 1,
	(2,"|"): [1, 3],
	(2, "-"): 2,
	(3,"\\"): 2,
	(3,"/"): 0,
	(3,"|"): 3,
	(3, "-"): [0, 2],
}

def energy(input, start):
	seen = []
	d = start[1]
	stack = [start]

	yl = len(input)
	xl = len(input[0])

	while len(stack) > 0:
		top = stack.pop(0)
		if top in seen:
			continue

		pos, d = top
		y, x = pos

		if 0<=y<yl and 0<=x<xl:
			seen.append(top)

		dy, dx = dirs[d]
		ny = y + dy
		nx = x + dx

		if 0<=ny<yl and 0<=nx<xl:
			c = input[ny][nx]
			nd = transform[(d, c)] if c != '.' else d

			# print(ny, nx, d, c, nd)

			if isinstance(nd, list):
				stack.insert(0, ((ny, nx), nd[0]))
				stack.append(((ny, nx), nd[1]))
			else:
				stack.insert(0, ((ny, nx), nd))

	t = list(set(map(lambda x: x[0], seen)))

	# rows = []
	# for y in range(yl):
	# 	row = []
	# 	for x in range(xl):
	# 		if (y, x) in t:
	# 			row.append("#")
	# 		else:
	# 			row.append(".")
	# 	rows.append("".join(row))
	# [print(i) for i in rows]
		
	return len(t)


@timer
@print_result
def part1(input):
	return energy(input, ((0, -1), 0))

@timer
@print_result
def part2(input):
	top = 0
	starts = []
	
	yl = len(input)
	xl = len(input[0])

	for y in range(yl):
		starts.append(((y, -1), 0))
		starts.append(((y, yl), 2))

	for x in range(xl):
		starts.append(((-1, x), 1))
		starts.append(((xl, x), 3))

	print(len(starts))
	# print(starts)

	# for start in starts:
	# 	e = energy(input, start)
	# 	if e > top:
	# 		top = e
	return top

def parse(input):
	return input

def main(args=None):
	data = init(path.dirname(__file__), inputs.read_to_str_arr, args)
	input = parse(data) 
	if isinstance(input, str):
		part1(input)
		part2(input)
	else:
		part1(input.copy())
		part2(input.copy())

if __name__ == "__main__":
	main(argv[1:])
