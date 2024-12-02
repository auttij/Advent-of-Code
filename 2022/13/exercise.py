import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from itertools import chain
from functools import cmp_to_key
from json import loads

def compare(a, b):
	if not a or not b:
		return bool(len(b)) - bool(len(a))

	av, bv, v = a[0], b[0], 0
	match (av, bv):
		case (list(), list()):
			v = compare(av, bv)
		case (list(), int()):
			v = compare(av, [bv])
		case (int(), list()):
			v = compare([av], bv)
		case (int(), int()):
			v = max(-1, min(1, bv - av))
	return v if v != 0 else compare(a[1:], b[1:])

@timer
@print_result
def exercise1(arr):
	return sum(i for i, (a, b) in enumerate(arr, start=1) if compare(a, b) == 1)

@timer
@print_result
def exercise2(arr):
	decoders = [[[2]], [[6]]]
	input = list(chain(*arr))
	input.extend(decoders)
	s = sorted(input, key=cmp_to_key(compare), reverse=True)
	return (s.index(decoders[0]) + 1) * (s.index(decoders[1]) + 1)

@timer
def main(args=None):
	s = init(path.dirname(__file__), inputs.read_to_str, args)
	arr = [[loads(i) for i in line.split()] for line in s.split('\n\n')]

	exercise1(arr.copy())
	exercise2(arr.copy())

if __name__ == "__main__":
	main(argv[1:])
