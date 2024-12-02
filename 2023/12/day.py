import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init

FP = {}
def f(str_in, num_in, i, bi, current):
	key = (i, bi, current)
	if key in FP:
		return FP[key]
	if i == len(str_in):
		if bi == len(num_in) and current == 0:
			return 1
		elif bi == len(num_in) - 1 and num_in[bi] == current:
			return 1
		else:
			return 0
		
	out = 0
	for c in ['.', '#']:
		if str_in[i] == c or str_in[i] == '?':
			if c == '.' and current == 0:
				out += f(str_in, num_in, i + 1, bi, 0)
			elif c == '.' and current > 0 and bi < len(num_in) and num_in[bi] == current:
				out += f(str_in, num_in, i + 1, bi + 1, 0)
			elif c == '#':
				out += f(str_in, num_in, i + 1, bi, current + 1)
	FP[key] = out
	return out


@timer
@print_result
def part1(s_i, n_i):
	occ = 0
	for i, s in enumerate(s_i):
		n = n_i[i]

		FP.clear()
		score = f(s, n, 0, 0, 0)
		occ += score
	return occ

def expand(s):
	return "?".join([s] * 5)

@timer
@print_result
def part2(s_i, n_i):
	occ = 0
	for i, line in enumerate(s_i):
		s = expand(line)
		n = n_i[i] * 5

		FP.clear()
		score = f(s, n, 0, 0, 0)
		occ += score
	return occ


def parse(input):
	strs = []
	nums = []
	for line in input:
		s, n = line.split(" ")
		strs.append(s)
		nums.append([int(i) for i in n.split(",")])
	return strs, nums


def main(args=None):
	arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
	s_i, n_i = parse(arr)
	part1(s_i, n_i)
	part2(s_i, n_i)

if __name__ == "__main__":
	main(argv[1:])
