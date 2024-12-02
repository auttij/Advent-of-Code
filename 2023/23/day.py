import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from aocHelpers.helpers import adjacent




@timer
@print_result
def part1(input):
	start = [(0, [i for i, x in enumerate(input[0]) if x == '.'][0])][0]
	target = ((len(input) - 1, len(input[0]) - 2))


	tr = {'>': (0, 1), 'v': (1, 0), '<': (0, -1), '^': (-1, 0)}
	def nei(pos, c):
		if c in tr:
			t = tr[c]
			return [(pos[0] + t[0], pos[1] + t[1])]
		
		n = [i for i in adjacent(pos)]
		return [(y, x) for y, x in n if 0<=y<len(input) and 0<=x<len(input[0]) and input[y][x] != '#']

	seen = {}
	stack = [(start, start, 0)]

	while len(stack):
		top = stack.pop()

		pos, prev, dist = top
		y, x = pos
		char = input[y][x]

		if pos not in seen or seen[pos] < dist:
			seen[pos] = dist

		neis = nei(pos, char)

		for n in neis:
			if n == prev:
				continue
			stack.append((n, pos, dist + 1))
	return seen[target]

def make_adjacencies(input):
	res = {}
	for i, row in enumerate(input):
		for j, c in enumerate(row):
			if c != '#':
				adj = dict()
				for y, x in adjacent((i, j)):
					if 0<=y<len(input) and 0<=x<len(input[0]):
						if input[y][x] != '#':
							adj[(y, x)] = 1
				res[(i, j)] = adj
	allkeys = list(res.keys())

	for key in allkeys:
		neighbors = res[key]
		if len(neighbors) == 2:
			left_neighbor, right_neighbor = neighbors.keys()
			del res[left_neighbor][key]
			del res[right_neighbor][key]
			res[left_neighbor][right_neighbor] = max(res[left_neighbor].get(right_neighbor, 0),  neighbors[left_neighbor] + neighbors[right_neighbor])
			res[right_neighbor][left_neighbor] = res[left_neighbor][right_neighbor]
			del res[key]
			
	return res

def dfs(graph, seen, current, target):
	if current == target:
		return sum(seen.values())
	best = None
	for neighbor in graph[current]:
		if neighbor in seen:
			continue
		seen[neighbor] = graph[current][neighbor]
		res = dfs(graph, seen, neighbor, target)
		if best is None or (res is not None and res > best):
			best = res
		del seen[neighbor]
	return best

@timer
@print_result
def part2(input):
	graph = make_adjacencies(input)
	return dfs(graph, {(1,1): 0}, (0, 1), (len(input) - 1, len(input[0]) - 2))

def main(args=None):
	input = init(path.dirname(__file__), inputs.read_to_str_arr, args)
	if isinstance(input, str):
		part1(input)
		part2(input)
	else:
		part1(input.copy())
		part2(input.copy())

if __name__ == "__main__":
	main(argv[1:])
