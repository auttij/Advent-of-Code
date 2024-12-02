import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init

@timer
@print_result
def exercise1(arr):
	lights = [[0 for i in range(1000)] for j in range(1000)]
	for cmd, (x1s, y1s), (x2s, y2s) in arr:
		x1, y1, x2, y2 = map(int, [x1s, y1s, x2s, y2s])
		if cmd == "off":
			for i in range(x1, x2 + 1):
				for j in range(y1, y2 + 1):
					lights[j][i] = 0
		if cmd == "on":
			for i in range(x1, x2 + 1):
				for j in range(y1, y2 + 1):
					lights[j][i] = 1
		if cmd == "toggle":
			for i in range(x1, x2 + 1):
				for j in range(y1, y2 + 1):
					lights[j][i] = abs(lights[j][i] - 1)
	return sum(map(sum, lights))
		

@timer
@print_result
def exercise2(arr):
	lights = [[0 for i in range(1000)] for j in range(1000)]
	for cmd, (x1s, y1s), (x2s, y2s) in arr:
		x1, y1, x2, y2 = map(int, [x1s, y1s, x2s, y2s])
		if cmd == "off":
			for i in range(x1, x2 + 1):
				for j in range(y1, y2 + 1):
					lights[j][i] = max(0, lights[j][i] - 1)
		if cmd == "on":
			for i in range(x1, x2 + 1):
				for j in range(y1, y2 + 1):
					lights[j][i] += 1
		if cmd == "toggle":
			for i in range(x1, x2 + 1):
				for j in range(y1, y2 + 1):
					lights[j][i] += 2
	return sum(map(sum, lights))

def main(args=None):
	input = init(path.dirname(__file__), inputs.read_to_str_arr, args)
	arr = []
	for line in input:
		f, *rest = line.split(" ")
		if f == "toggle":
			arr.append(("toggle", rest[0].split(","), rest[-1].split(",")))
		else:
			arr.append((rest[0], rest[1].split(","), rest[-1].split(",")))
	exercise1(arr[::])
	exercise2(arr[::])

if __name__ == "__main__":
	main(argv[1:])
