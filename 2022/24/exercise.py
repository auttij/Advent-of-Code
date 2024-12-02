import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from aocHelpers.helpers import adjacent
from collections import deque
from itertools import chain
from math import lcm

dirs = { "<": -1, ">": 1, "^": -1j, "v": 1j, "": 0 }
def bfs(start, end, safeTimes, timeWrap, startTime):
    queue = [(start, startTime)]
    seen = set()

    while queue:
        pos, time = queue.pop(0)

        if pos == end:
            return time

        if (pos, time) in seen:
            continue

        seen.add((pos, time))
        new_time = time + 1

        for direction in dirs.values():
            new_pos = pos + direction

            if new_pos in safeTimes and (new_time % timeWrap) in safeTimes[new_pos]:
                queue.append((new_pos, new_time))

    raise ValueError("No path found")

@timer
@print_result
def exercise1(start, end, safeTimes, timeWrap):
	return bfs(start, end, safeTimes, timeWrap, 0)

@timer
@print_result
def exercise2(start, end, safeTimes, timeWrap, time):
	time2 = bfs(end, start, safeTimes, timeWrap, time)
	return bfs(start, end, safeTimes, timeWrap, time2)

def main(args=None):
	grid = init(path.dirname(__file__), inputs.read_to_str_arr, args)
	rows, cols = len(grid), len(grid[0])
	timeWrap = lcm(rows - 2, cols - 2)
	
	start, end = grid[0].index("."), grid[-1].index(".") + (len(grid) - 1) * 1j
	safeTimes = {
		x + y * 1j: set(range(timeWrap)) for y in range(rows) for x in range(cols)
    }

	for y, row in enumerate(grid):
		for x, cell in enumerate(row):
			position = x + y * 1j

			if cell == "#":
				safeTimes[position] = set()
				continue

			if cell == ".":
				continue

			direction = dirs[cell]

			for t in range(timeWrap):
				safeTimes[position].discard(t)

				position += direction
				# wrap within internal grid
				position = complex(
					(position.real - 1) % (cols - 2) + 1,
					(position.imag - 1) % (rows - 2) + 1,
				)

	time = exercise1(start, end, safeTimes, timeWrap)
	exercise2(start, end, safeTimes, timeWrap, time)

if __name__ == "__main__":
	main(argv[1:])
