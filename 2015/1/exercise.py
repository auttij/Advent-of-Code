import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init

@timer
@print_result
def exercise1(arr):
	return arr.count('(') - arr.count(')')

@timer
@print_result
def exercise2(arr):
	count = 0
	for i, val in enumerate(arr):
		if count == -1:
			return i
		if val == '(':
			count += 1
		else:
			count -= 1

def main(args=None):
	arr = init(path.dirname(__file__), inputs.read_to_str, args)
	exercise1(arr)
	exercise2(arr)

if __name__ == "__main__":
	main(argv[1:])
