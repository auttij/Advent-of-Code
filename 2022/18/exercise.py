import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init

def adj(pos):
    for axis in range(3):
        for d in (-1, 1):
            q = list(pos)
            q[axis] += d
            yield tuple(q)

@timer
@print_result
def exercise1(arr):
	return sum(1 for pos in arr for q in adj(pos) if q not in arr)

@timer
@print_result
def exercise2(arr):
	# find corners furthest away from each other
	minTuple = tuple(min(pos[axis] for pos in arr) - 1 for axis in range(3))
	maxTuple = tuple(max(pos[axis] for pos in arr) + 1 for axis in range(3))
	
	# dfs from corner to corner, find all reachable positions on the way
	stack = [minTuple]
	visited = set()
	exposed = 0
	while stack:
		pos = stack.pop()
		if pos in visited:
			continue
		visited.add(pos)
		for q in adj(pos):
			if q in arr:
				exposed += 1
			if q not in arr \
				and q not in visited \
				and all(l <= v <= u for l, v, u in zip(minTuple, q, maxTuple)):
					stack.append(q)
	return exposed

def main(args=None):
	arr = set(init(path.dirname(__file__), inputs.read_to_int_tuple_arr, args))
	exercise1(arr)
	exercise2(arr)

if __name__ == "__main__":
	main(argv[1:])
