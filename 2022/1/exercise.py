import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init

@timer
@print_result
def exercise1(arr):
	return max(map(sum, arr))

@timer
@print_result
def exercise2(arr):
	elves =  sorted(map(sum, arr))
	return sum(elves[-3:])

def main(args=None):
	arr = init(path.dirname(__file__), inputs.read_to_2d_int_arr, args)
	exercise1(arr.copy())
	exercise2(arr.copy())

if __name__ == "__main__":
	main(argv[1:])
