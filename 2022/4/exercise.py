import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init

@timer
@print_result
def exercise1(arr):
	count = 0
	for s1, e1, s2, e2 in arr:
		if s1 <= s2 and e2 <= e1 or s2 <= s1 and e1 <= e2:
			count += 1
	return count

@timer
@print_result
def exercise2(arr):
	count = 0
	for s1, e1, s2, e2 in arr:
		# (s2,e2) overlaps (s1,e1) if it is not completely to the left or completely to the right
		#          s2 -- e2
		#    e1              s1
		if not (e1 < s2 or s1 > e2):
			count += 1
	return count

def main(args=None):
	arr = init(path.dirname(__file__), inputs.read_to_int_tuple_arr, args)
	exercise1(arr.copy())
	exercise2(arr.copy())

if __name__ == "__main__":
	main(argv[1:])
