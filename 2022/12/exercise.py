import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from aocHelpers.helpers import bfs

def parseGrid(arr):
	aList = []
	start = end = None
	for i, row in enumerate(arr):
		for j, v in enumerate(row):
			if v == "S":
				start = (i, j)
				aList.append((i, j))
				arr[i][j] = "a"
			elif v == "E":
				end = (i, j)
				arr[i][j] = "z"
			elif v == "a":
				aList.append((i, j))
	return arr, start, end, aList

def comparisonFn(a, b):
	return -2 <= ord(a) - ord(b) <= 1

@timer
@print_result
def exercise1(GRID, START, END, _):
	return bfs(GRID, START, END, comparisonFn)

@timer
@print_result
def exercise2(GRID, _, END, A_LIST):
	out = [bfs(GRID, a, END, comparisonFn) for a in A_LIST]
	return min(out)

@timer
def main(args=None):
	arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
	input = list(map(list, arr.copy()))
	GRID, START, END, A_LIST = parseGrid(input)

	exercise1(GRID, START, END, A_LIST)
	exercise2(GRID, START, END, A_LIST)

if __name__ == "__main__":
	main(argv[1:])
