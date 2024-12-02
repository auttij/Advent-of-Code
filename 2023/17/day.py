import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from heapq import heappush,heappop

north = (-1, 0)
south = (1, 0)
west = (0, -1)
east = (0, 1)
dirs = [east, south, west, north]
poss = [[0, 1, 3], [1, 0, 2], [2, 1, 3], [3, 2, 0]]

seen = {}

def neigh(node, g, ultra):
    y, x, v, dir = node
    dy, dx = dir
    left, right = (-dy,dx), (dy,-dx)
    if v < (10 if ultra else 3) and 0<=y+dy<len(g) and 0<=x+dx<len(g[0]):
        yield (y + dy, x + dx, v + 1, dir), int(g[y+dy][x+dx])

    for dx, dy in left, right:
        if 0<=y+dy<len(g) and 0<=x+dx<len(g[0]) and (not ultra or v > 3):
            yield (y + dy, x + dx, 1, (dy, dx)), int(g[y+dy][x+dx])

def pathfind(g, ultra):
	seen = set()
	start1, start2 = (0, 0, 0, (east)), ((0, 0, 0, (south)))
	dist = {start1: 0, start2: 0}
	Q = [(0, start1), (0, start2)]
	target = (len(g) - 1, len(g[0]) - 1)

	while len(Q):
		_, u = heappop(Q)
		if u in seen: 
			continue
		seen.add(u)

		if u[:2] == target and (not ultra or u[2] > 3):
			target = u
			break
		for v, cost in neigh(u, g, ultra):
			if v in seen:
				continue

			alt = dist[u] + cost
			if v not in dist or alt < dist[v]:
				dist[v] = alt
				heappush(Q, (alt, v))
	return dist[target]


@timer
@print_result
def part1(g):
	return pathfind(g, False)

@timer
@print_result
def part2(g):
	return pathfind(g, True)

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
