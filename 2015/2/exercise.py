import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init

@timer
@print_result
def exercise1(arr):
	total = 0
	for l, w, h in arr:
		sides = [2*l*w, 2*l*h, 2*w*h]
		total += sum(sides) + int(min(sides)/2)
	return total

@timer
@print_result
def exercise2(arr):
	total = 0
	for l, w, h in arr:
		total += 2*sum(sorted([l, w, h])[:2]) + (l*w*h)
	return total

def main(args=None):
	arr = init(path.dirname(__file__), inputs.read_to_int_tuple_arr, args)
	exercise1(arr.copy())
	exercise2(arr.copy())

if __name__ == "__main__":
	main(argv[1:])
