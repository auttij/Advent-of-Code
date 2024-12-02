import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init

@timer
@print_result
def exercise1(arr):
	s = 0	
	for line in arr:
		asd = []
		for char in line:
			if char.isdigit():
				asd.append(char)
		s += int(asd[0] + asd[-1], 10)
	return s

@timer
@print_result
def exercise2(arr):
	nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
	s = 0
	for line in arr:
		digits = []

		for i, char in enumerate(line):
			if char.isdigit():
				digits.append(char)

			for d, num in enumerate(nums):
				if line[i:].startswith(num):
					digits.append(str(d))

		s += int(digits[0] + digits[-1], 10)
	return s


def main(args=None):
	arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
	exercise1(arr)
	exercise2(arr)

if __name__ == "__main__":
	main(argv[1:])
