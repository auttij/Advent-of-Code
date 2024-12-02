import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init

@timer
@print_result
def part1(input):
	l = zip(input[0], input[1])
	out = 1
	for time, dist in l:
		distances = [t * (time - t) for t in range(time)]
		wins = [d for d in distances if d > dist]
		out *= len(wins)
	return out

@timer
@print_result
def part2(input):
	time = int("".join([str(i) for i in input[0]]))
	dist = int("".join([str(i) for i in input[1]]))
	
	def bs(lo, hi, clause):
		while lo <= hi:
			m = int((lo + hi) // 2)
			if clause(m):
				lo = m + 1
			elif not clause(m):
				hi = m - 1
			else:
				return m
		return m

	def search_lo(m):
		return (time - m) * m < dist

	def search_hi(m):
		return (time - m) * m > dist

	lo = bs(0, time/2, search_lo)
	hi = bs(time/2, time, search_hi)
	return hi - lo + 1


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
