import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
import re

@timer
@print_result
def exercise1(arr):
	def iterate(word):
		vowels = False
		double = False
		disallowed = False
		vc = 0
		for i, e in enumerate(word):
			if (not vowels) and (e in "aeiou"):
				vc += 1
				if vc >= 3:
					vowels = True

			if i < 15:
				if e + word[i+1] in ["ab", "cd", "pq", "xy"]:
					disallowed = True
				if e == word[i+1]:
					double = True
			
		return vowels and double and not disallowed
		
	return len(list(filter(iterate, arr)))

@timer
@print_result
def exercise2(arr):
	def f(word):
		return re.search(r'(..).*\1', word) and re.search(r'(.).\1', word)
	return len(list(filter(f, arr)))

def main(args=None):
	arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
	exercise1(arr[::])
	exercise2(arr[::])

if __name__ == "__main__":
	main(argv[1:])
