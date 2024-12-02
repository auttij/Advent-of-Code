import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init

@timer
@print_result
def exercise1(arr):
	out = 0
	for line in arr:
		# print(eval(line), line)
		out += len(line) - len(eval(line))
	return out

@timer
@print_result
def exercise2(arr):
	out = 0
	for line in arr:
		s = '"{}"'.format(line.replace('\\', '\\\\').replace('\"', '\\\"'))
		out += len(s) - len(line)
	return out

def main(args=None):
	arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
	exercise1(arr[::])
	exercise2(arr[::])

if __name__ == "__main__":
	main(argv[1:])
