import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init

@timer
@print_result
def exercise1(arr):
	seen = set()
	x, y = 0, 0
	seen.add((x, y))
	for i in arr:
		if i == "^":
			y += 1
		elif i == "v":
			y -= 1
		elif i == ">":
			x += 1
		elif i == "<":
			x -= 1
		seen.add((x, y))
	return len(seen)

@timer
@print_result
def exercise2(arr):
	seen = set()
	x, y = 0, 0

	seen.add((x, y))
	for i in arr[::2]:
		if i == "^":
			y += 1
		elif i == "v":
			y -= 1
		elif i == ">":
			x += 1
		elif i == "<":
			x -= 1
		seen.add((x, y))
		
	x, y = 0, 0
	for i in arr[1::2]:
		if i == "^":
			y += 1
		elif i == "v":
			y -= 1
		elif i == ">":
			x += 1
		elif i == "<":
			x -= 1
		seen.add((x, y))
	return len(seen)

def main(args=None):
	arr = init(path.dirname(__file__), inputs.read_to_str, args)
	exercise1(arr)
	exercise2(arr)

if __name__ == "__main__":
	main(argv[1:])
