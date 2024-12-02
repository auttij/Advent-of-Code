import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init

@timer
@print_result
def exercise1(arr):
	lines = arr.split("\n")
	games= {}

	out = 0


	for game in lines:
		a, b = game.split(":")
		game_num = int(a.split(" ")[1])
		games[game_num] = {"red": 0, "green": 0, "blue": 0}
		sets = [i.strip() for i in b.split(";")]
		for s in sets:
			tops = {"red": 0, "green": 0, "blue": 0}
			draws = s.split(", ")
			for draw in draws:
				num, color = draw.split(" ")
				tops[color] += int(num)

			for color, num in tops.items():	
				if tops[color] > games[game_num][color]:
					games[game_num][color] = tops[color]
		if games[game_num]["red"] <= 12 and games[game_num]["green"] <= 13  and games[game_num]["blue"] <= 14:
			out += game_num
	return out


@timer
@print_result
def exercise2(arr):
	lines = arr.split("\n")
	games= {}

	out = 0


	for game in lines:
		a, b = game.split(":")
		game_num = int(a.split(" ")[1])
		games[game_num] = {"red": 0, "green": 0, "blue": 0}
		sets = [i.strip() for i in b.split(";")]
		for s in sets:
			tops = {"red": 0, "green": 0, "blue": 0}
			draws = s.split(", ")
			for draw in draws:
				num, color = draw.split(" ")
				tops[color] += int(num)

			for color, num in tops.items():	
				if tops[color] > games[game_num][color]:
					games[game_num][color] = tops[color]
		out += games[game_num]["red"] * games[game_num]["green"] * games[game_num]["blue"]
	return out

def main(args=None):
	arr = init(path.dirname(__file__), inputs.read_to_str, args)
	exercise1(arr)
	exercise2(arr)

if __name__ == "__main__":
	main(argv[1:])
