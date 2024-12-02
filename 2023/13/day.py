import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from aocHelpers.helpers import transpose



def find_reflection(input):
	possible = [i for i in range(len(input[0]) - 1)]
	row = 0
	while len(possible) > 0 and row < len(input):
		new_pos = []
		for i in possible:
			if input[row][i] == input[row][i + 1]:
				new_pos.append(i)

		row += 1
		possible = new_pos

	row = 0
	while len(possible) > 0 and row < len(input):
		new_pos = []
		for i in possible:
			j = 1
			poss = True
			while 0<=i-j and i+j+1<len(input[0]):
				if input[row][i-j] != input[row][i+1+j]:
					poss = False
				j += 1
			if poss:
				new_pos.append(i)
		possible = new_pos
		row += 1

	if len(possible) == 1:
		return possible[0] + 1
	

@timer
@print_result
def part1(input):
	patterns = [p for p in input.split("\n\n")]
	out = 0

	for p in patterns:
		rows = [r for r in p.split("\n")]

		col = find_reflection(rows)
		if col:
			out += col

		row = find_reflection(transpose(rows))
		if row:
			out += 100 * row
	return out

def find_reflection_smudge(input, original):
	possible = [i for i in range(len(input[0]) - 1) if i is not original]
	possible = [(i, None) for i in possible]

	row = 0
	while len(possible) > 0 and row < len(input):
		new_pos = []
		for i, smudge in possible:
			if input[row][i] == input[row][i + 1]:
				new_pos.append((i, smudge))
			elif smudge == None:
				new_pos.append((i, (row, i)))
		row += 1
		possible = new_pos

	row = 0
	while len(possible) > 0 and row < len(input):
		new_pos = []
		for i, smudge in possible:
			j = 1
			poss = True
			while 0<=i-j and i+j+1<len(input[0]):
				if input[row][i-j] != input[row][i+1+j]:
					if smudge == None:
						smudge = (row, i-j)
					else:
						poss = False
				j += 1
			if poss:
				new_pos.append((i, smudge))
		possible = new_pos
		row += 1

	if len(possible) == 1:
		return possible[0][0] + 1

@timer
@print_result
def part2(input):
	patterns = [p for p in input.split("\n\n")]
	out = 0

	for p in patterns:
		rows = [r for r in p.split("\n")]
		col_orig = find_reflection(rows)
		col = 0
		if col_orig:
			col = find_reflection_smudge(rows, col_orig - 1)
		else:
			col = find_reflection_smudge(rows, -1)
		if col:
			out += col

		t = transpose(rows)
		row_orig = find_reflection(t)
		row = 0
		if row_orig:
			row = find_reflection_smudge(t, row_orig - 1)
		else:
			row = find_reflection_smudge(t, -1)

		if row:
			out += 100 * row
	return out

def main(args=None):
	input = init(path.dirname(__file__), inputs.read_to_str, args)
	part1(input)
	part2(input)

if __name__ == "__main__":
	main(argv[1:])
