import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init

@timer
@print_result
def exercise1(arr):
	for i, d in enumerate(arr[3:], start=3):
		a, b, c  = arr[i-3], arr[i-2], arr[i-1]
		if len(set([a, b, d, c])) == 4:
			print(set([a, b, c, d]))
			return i + 1
 
@timer
@print_result
def exercise2(arr):
	length = 13
	for i, d in enumerate(arr[length:], start=length):
		l = arr[i-length:i+1]
		if len(set(l)) == length + 1:
			return i + 1

def main(args=None):
	arr = init(path.dirname(__file__), inputs.read_to_str, args)
	exercise1(arr)
	exercise2(arr)

if __name__ == "__main__":
	main(argv[1:])
