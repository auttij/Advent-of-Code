import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init

def get_highest(games):
	highest = []
	for game in games:
		top = { "red": 0, "green": 0, "blue": 0 }
		for num, col in game:
			if top[col] < num:
				top[col] = num
		highest.append(top)
	return highest

@timer
@print_result
def part1(highest):
	out = 0
	for i, game in enumerate(highest, start=1):
		red, green, blue = game.values()
		if red <= 12 and green <= 13 and blue <= 14:
			out += i

	return out

@timer
@print_result
def part2(highest):
	out = 0
	for game in highest:
		red, green, blue = game.values()
		out += red * green * blue

	return out


def parse(input):
	games = []

	for line in input:
		game_num, rest = line.split(": ")
		sets = rest.replace(';', ',').split(", ")
		as_tuples = [(int(i), c) for pick in sets for i, c in [pick.split(" ")]]
		games.append(as_tuples)
	return games


def main(args=None):
	arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
	input = parse(arr)
	highest = get_highest(input)

	part1(highest)
	part2(highest)

if __name__ == "__main__":
	main(argv[1:])
