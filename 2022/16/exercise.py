import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from aocHelpers.helpers import dfs
from functools import lru_cache
from itertools import chain

def floydWarshall(targets):
	dist = [[99 for i in range(len(targets))] for j in range(len(targets))]
	for vi, targs in enumerate(targets):
		for target in targs:
			dist[vi][target] = 1
		dist[vi][vi] = 0
	for k in range(len(targets)):
		for i in range(len(targets)):		
			for j in range(len(targets)):
				if dist[i][j] > dist[i][k] + dist[k][j]:
					dist[i][j] = dist[i][k] + dist[k][j]
	return dist

def exercise(arr):
	ind = { a: i for i, (a, b, c) in enumerate(arr)}
	og = [a for (a, b, c) in arr]
	targets = [[ind[ci] for ci in c] for a, b, c in arr]
	pressures = [int(b) for a, b, c in arr]

	dist = floydWarshall(targets)
	start = ind['AA']
	l = tuple(filter(lambda x: pressures[x] > 0, map(lambda x: x[0], enumerate(pressures))))

	# print(", ".join([og[i] for i in range(10)]))
	# for i, row in enumerate(dist):
	# 	print(", ".join([str(val).rjust(2,"0") for val in row]), end=" ")
	# 	print(og[i])
	# print("non-zero:", [og[i] for i in l])

	def chooseOne(xl):
		for i in range(len(xl)):
			yield (xl[i], xl[:i] + xl[i+1:])

	def gen(cur, rest, time):
		for i, rr in chooseOne(rest):
			if dist[cur][i] < time:
				yield pressures[i] * (time - dist[cur][i] - 1) + dfs(i, rr, time - dist[cur][i] - 1)

	@lru_cache(maxsize=100000000)
	def dfs(cur, rest, time):
		return max(gen(cur, rest, time), default=0)


	def gen2(cur, rest, time):
		for i, rr in chooseOne(rest):
			if dist[cur][i] < time:
				yield pressures[i] * (time - dist[cur][i] - 1) + dfs2(i, rr, time - dist[cur][i] - 1)

	@lru_cache(maxsize=100000000)
	def dfs2(cur, rest, time):
		return max(gen2(cur, rest, time), default=dfs(start, rest, 26))

	@timer
	@print_result
	def exercise1():
		return dfs(start, l, 30)
	exercise1() # 1651 / 1944

	@timer
	@print_result
	def exercise2():
		return dfs2(start, l, 26)
	exercise2() # 1707 / 2679

def main(args=None):
	input = init(path.dirname(__file__), inputs.read_to_str_arr, args)
	arr = []
	for line in input:
		a = line.split()
		subArr = [a[1], a[4].split("=")[1][:-1]]
		subArr.append("".join(a[9:]).split(","))
		arr.append(subArr)
	exercise(arr)

if __name__ == "__main__":
	main(argv[1:])
