import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from aocHelpers.helpers import neighbors2d as neighbors

def moveNorth(pos, elfSet):
	d = ((-1, 0), (-1, 1), (-1, -1))
	newPos = set([(pos[0] + r, pos[1] + c) for r, c in d])
	return 0 if elfSet & newPos else (pos[0] - 1, pos[1])

def moveSouth(pos, elfSet):
	d = ((1, 0), (1, 1), (1, -1))
	newPos = set([(pos[0] + r, pos[1] + c) for r, c in d])
	return 0 if elfSet & newPos else (pos[0] + 1, pos[1])
	
def moveWest(pos, elfSet):
	d = ((0, -1), (-1, -1), (1, -1))
	newPos = set([(pos[0] + r, pos[1] + c) for r, c in d])
	return 0 if elfSet & newPos else (pos[0], pos[1] - 1)

def moveEast(pos, elfSet):
	d = ((0, 1), (1, 1), (-1, 1))
	newPos = set([(pos[0] + r, pos[1] + c) for r, c in d])
	return 0 if elfSet & newPos else (pos[0], pos[1] + 1)

funcs = [moveNorth, moveSouth, moveWest, moveEast]
funcsLen = len(funcs)
def move(pos, elfSet, funcs, fStart):
	for f in range(funcsLen):
		newPos = funcs[(fStart + f) % funcsLen](pos, elfSet)
		if newPos != 0:
			return newPos
	return 0

def draw(positions):
	sp = set(positions)
	yList = list(map(lambda x: x[0], positions))
	xList = list(map(lambda x: x[1], positions))
	minY, maxY = min(yList), max(yList)
	minX, maxX = min(xList), max(xList)
	# print(positions, minY, minX, maxY, maxX)
	for r in range(minY, maxY + 1):
		row = ""
		for c in range(minX, maxX + 1):
			if set([(r, c)]) & sp:
				row += "#"
			else:
				row += "."
		print(row)
	print()

def solve(input, part):
	fStart = 0
	positions = input
	newPos = [-1 for i in positions]

	iter = 0
	while any(newPos):
		seen = set()
		dupePos = {}
		iter += 1
		# draw(positions)

		elfSet = set(positions)
		for ei, elf in enumerate(positions):
			nei = set(neighbors(elf))

			if not elfSet & nei:
				# nothing around, don't move
				newPos[ei] = 0
				seen.add(elf)
				dupePos[elf] = ei
			else:
				# another elf adjacent, move 
				np = move(elf, elfSet, funcs, fStart)
				nps = set([np])
				if np == 0:
					# something was in the way in every direction
					seen.add(elf)
					dupePos[elf] = ei
					newPos[ei] = 0
				elif seen & nps:
					# anoter elf is trying to move to same position
					newPos[dupePos[np]] = 0
					newPos[ei] = 0
				else:
					# position free, move
					seen.add(np)
					dupePos[np] = ei
					newPos[ei] = np
		
		# Update new positions
		positions = [val if val else positions[i] for i, val in enumerate(newPos)]
		newPos = [-1 if i != 0 else 0 for i in newPos]
		fStart += 1
		# funcs.append(funcs.pop(0))

		if part == 1 and iter == 9:
			yList = list(map(lambda x: x[0], positions))
			xList = list(map(lambda x: x[1], positions))
			minY, maxY = min(yList), max(yList)
			minX, maxX = min(xList), max(xList)
			return ((maxY - minY + 1) * (maxX - minX + 1)) - len(positions)
	return iter

@timer
@print_result
def exercise1(input):
	return solve(input, 1)

@timer
@print_result
def exercise2(input):
	return solve(input, 2)

def main(args=None):
	arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
	input = []
	for r, row in enumerate(arr):
		for c, v in enumerate(row):
			if v == '#':
				input.append((r, c))

	exercise1(input)
	exercise2(input)

if __name__ == "__main__":
	main(argv[1:])
