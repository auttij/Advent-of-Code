import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from aocHelpers.helpers import neighbors2d


def parse_locations(arr, comp_func):
	line_len = len(arr[0])
	symbols = []
	numbers = []
	num_positions = []

	for y, line in enumerate(arr):
		num = []
		num_pos = []
		for x, c in enumerate(line):
			# get any symbol pos in part 1, * in part 2
			if comp_func(c):
				symbols.append((y, x))

			if c.isdigit():
				num.append(c)
				num_pos.append((y, x))

				# all numbers are horizontal. 
				# if last number in a sequence, combine array to one number
				if x == line_len - 1 or not line[x + 1].isdigit():
					numbers.append(int("".join(num)))
					num = []
					num_positions.append(num_pos)
					num_pos = []

	return symbols, numbers, num_positions

def iterate_neighbors(symbols, numbers, num_positions):
	adjacent_number_sum = 0
	gear_neighbors = {}

	seen = []
	for gi, pos in enumerate(symbols):
		neighbors = tuple(neighbors2d(pos))
		gear_neighbors[gi] = []

		for nei in neighbors:		
			for i, num_pos_arr in enumerate(num_positions):
				if nei in num_pos_arr:
					if numbers[i] not in gear_neighbors[gi]:
						gear_neighbors[gi].append(numbers[i])

					if i not in seen:
						adjacent_number_sum += numbers[i]
						seen.append(i)

	return adjacent_number_sum, gear_neighbors
	

@timer
@print_result
def exercise1(arr):
	def comp_function(c):
		return not c.isdigit() and c != '.'

	symbols, numbers, num_positions = parse_locations(arr, comp_function)
	adjacent_number_sum, _ = iterate_neighbors(symbols, numbers, num_positions)
	return adjacent_number_sum

@timer
@print_result
def exercise2(arr):
	def comp_function(c):
		return c == '*'

	symbols, numbers, num_positions = parse_locations(arr, comp_function)
	_, gear_neighbors = iterate_neighbors(symbols, numbers, num_positions)
	
	ratio = 0
	for numbers in gear_neighbors.values():
		if len(numbers) == 2:
			ratio += numbers[0] * numbers[1]
	return ratio


def main(args=None):
	arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
	exercise1(arr.copy())
	exercise2(arr.copy())

if __name__ == "__main__":
	main(argv[1:])
