import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init

@timer
@print_result
def exercise1(dist):
	def chooseOne(l):
		for i in range(len(l)):
			yield (l[i], l[:i] + l[i+1:])

	def gen(cur, rest, total):
		for r, rr in chooseOne(rest):
			yield dist[cur][r] + dfs(r, rr, total + dist[cur][r])

	def dfs(cur, rest, total):
		return min(gen(cur, rest, total), default=0)
	return min(dfs(i, rest, 0) for i, rest in chooseOne(list(range(8))))


@timer
@print_result
def exercise2(dist):
	def chooseOne(l):
		for i in range(len(l)):
			yield (l[i], l[:i] + l[i+1:])

	def gen(cur, rest, total):
		for r, rr in chooseOne(rest):
			yield dist[cur][r] + dfs(r, rr, total + dist[cur][r])

	def dfs(cur, rest, total):
		return max(gen(cur, rest, total), default=0)

	return max(dfs(i, rest, 0) for i, rest in chooseOne(list(range(8))))

def main(args=None):
	arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
	ind = 0
	keys = {}

	size = 8
	dist = [[9999 for j in range(size)] for i in range(size)]

	for line in arr:
		key1, _, key2, _, distance = line.split()
		if key1 not in keys:
			keys[key1] = ind
			ind += 1
		if key2 not in keys:
			keys[key2] = ind
			ind += 1
		dist[keys[key1]][keys[key2]] = int(distance)
		dist[keys[key2]][keys[key1]] = int(distance)
	
	print(dist)
	exercise1(dist[::])
	exercise2(dist[::])

if __name__ == "__main__":
	main(argv[1:])
