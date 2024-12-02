import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init

def parse(arr):
	out = []
	for line in arr:
		parts = line.split(' -> ')
		out.append([list(map(int, part.split(','))) for part in parts])
	return out


@timer
@print_result
def exercise1(arr):
	minX, maxX = 999, 0
	minY, maxY = 999, 0
	for line in arr:
		for a, b in line:
			if a < minX:
				minX = a
			elif a > maxX:
				maxX = a
			if b < minY:
				minY = b
			elif b > maxY:
				maxY = b
	print(minX, maxX)
	print(minY, maxY)

	lenX = maxX - minX + 2
	waterfall = [['.' for i in range(lenX)] for i in range(maxY + 1)]

	for line in arr:
		prevX, prevY = 0, 0

		for a, b in line:
			x = a - minX + 1
			y = b
			if prevX and prevY:
				for i in range(prevX, x):
					waterfall[y][i] = '#'
				for i in range(x, prevX):
					waterfall[y][i] = '#'
				for j in range(prevY, y):
					waterfall[j][x] = '#'
				for j in range(y, prevY):
					waterfall[j][x] = '#'
			# print(x, y, (a, b))
			waterfall[y][x] = '#'
			prevX, prevY = x, y

	def dropSand():
		x = 500 - minX + 1
		y = 0
		while True:
			if y == maxY:
				return 0
			elif waterfall[y + 1][x] == '.':
				y += 1
			elif waterfall[y + 1][x - 1] == '.':
				y += 1
				x -= 1
			elif waterfall[y + 1][x + 1] == '.':
				y += 1
				x += 1
			else:
				waterfall[y][x] = 'o'
				return 1

	sand = 0
	while dropSand():
		sand += 1
	
	for line in waterfall:
		logging.debug("".join(line))
	return sand

@timer
@print_result
def exercise2(arr):
	minX, maxX = 999, 0
	minY, maxY = 999, 0
	for line in arr:
		for a, b in line:
			if a < minX:
				minX = a
			elif a > maxX:
				maxX = a
			if b < minY:
				minY = b
			elif b > maxY:
				maxY = b
	print(minX, maxX)
	print(minY, maxY)

	lenX = maxX + 95
	waterfall = [['.' for i in range(lenX)] for i in range(maxY + 3)]
	for x in range(0, lenX):
		waterfall[maxY + 2][x] = '#'

	for line in arr:
		prevX, prevY = 0, 0

		for a, b in line:
			x = a
			y = b
			if prevX and prevY:
				for i in range(prevX, x):
					waterfall[y][i] = '#'
				for i in range(x, prevX):
					waterfall[y][i] = '#'
				for j in range(prevY, y):
					waterfall[j][x] = '#'
				for j in range(y, prevY):
					waterfall[j][x] = '#'
			# print(x, y, (a, b))
			waterfall[y][x] = '#'
			prevX, prevY = x, y

	def dropSand():
		x = 500
		y = 0
		while True:
			if waterfall[y + 1][x] == '.':
				y += 1
			elif waterfall[y + 1][x - 1] == '.':
				y += 1
				x -= 1
			elif waterfall[y + 1][x + 1] == '.':
				y += 1
				x += 1
			elif y == 0:
				waterfall[y][x] = 'o'
				return 0
			else:
				waterfall[y][x] = 'o'
				return 1

	sand = 1
	while dropSand():
		sand += 1
	
	# for line in waterfall:
	# 	logging.debug("".join(line))
	return sand

def main(args=None):
	arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
	input = parse(arr)
	exercise1(input.copy())
	exercise2(input.copy())

if __name__ == "__main__":
	main(argv[1:])
