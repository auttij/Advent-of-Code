import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from aocHelpers.helpers import adjacent

tr = {
	"R": (0, 1),
	"D": (1, 0),
	"L": (0, -1),
	"U": (-1, 0)
}

def shoelace(input):
	area = 0
	perimeter = 0
	y, x = 0, 0
	for d, length in input:
		dy, dx = tr[d]
		dy, dx = dy*length, dx*length
		y, x = y+dy, x+dx
		perimeter += length
		area += x*dy

	return area + perimeter//2 + 1

@timer
@print_result
def part1(input):
	return shoelace(input)

@timer
@print_result
def part2(input):
	return shoelace(input)

def parse(data):
	dirs= { '0': 'R', '1': 'D', '2': 'L', '3': 'U' }
	input_1 = []
	input_2 = []
	for line in data:
		d, n, c = line.split(" ")
		input_1.append((d, int(n)))
		input_2.append((dirs[c[-2]], int(c[2:-2], 16)))
	return input_1, input_2

def main(args=None):
	data = init(path.dirname(__file__), inputs.read_to_str_arr, args)
	input_1, input_2 = parse(data)
	part1(input_1)
	part2(input_2)

if __name__ == "__main__":
	main(argv[1:])
