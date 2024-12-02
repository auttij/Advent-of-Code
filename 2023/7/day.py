import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from collections import Counter

class Camel:
	def __init__(self, cards, bid, conv, jokers):
		cpy = cards
		
		highest_hand = cards
		highest_type = 0

		it = conv.keys() if "J" else ["J"]
		for crd in it:
			test_hand = cpy.replace("J", crd)

			c = Counter([x for x in test_hand])
			
			t = list(sorted(c.values()))
			
			if t == [5] and highest_type <= 6:
				highest_type = 6
				highest_hand = test_hand
			elif t == [1, 4] and highest_type <= 5:
				highest_type = 5
				highest_hand = test_hand
			elif t == [2, 3] and highest_type <= 4:
				highest_type = 4
				highest_hand = test_hand
			elif t == [1, 1, 3] and highest_type <= 3:
				highest_type = 3
				highest_hand = test_hand
			elif t == [1, 2, 2] and highest_type <= 2:
				highest_type = 2
				highest_hand = test_hand
			elif t == [1, 1, 1, 2] and highest_type <= 1:
				highest_type = 1
				highest_hand = test_hand
			elif t == [1, 1, 1, 1, 1] and highest_type <= 0:
				highest_type = 0
				highest_hand = test_hand

		self.hand = highest_hand
		self.type = highest_type

		self.score = 0
		self.bid = int(bid)

		for i, v in enumerate(cards, start=1):
			self.score += (13 ** (5 - i)) * conv[v]

		self.score += (13 ** 5) * self.type

@timer
@print_result
def part1(input):
	CONV = {
		"2": 1,
		"3": 2,
		"4": 3,
		"5": 4,
		"6": 5,
		"7": 6,
		"8": 7,
		"9": 8,
		"T": 9,
		"J": 10,
		"Q": 11,
		"K": 12,
		"A": 13,
	}

	lines = [i.split(" ") for i in input]
	camels = [Camel(cards, bid, CONV, False) for cards, bid in lines]

	camels.sort(key=lambda x: x.score, reverse=False)
	out = 0
	for i, c in enumerate(camels, start=1):
		out += c.bid * i
	return out


@timer
@print_result
def part2(input):
	CONV = {
		"J": 0,
		"2": 1,
		"3": 2,
		"4": 3,
		"5": 4,
		"6": 5,
		"7": 6,
		"8": 7,
		"9": 8,
		"T": 9,
		"Q": 10,
		"K": 11,
		"A": 12,
	}

	lines = [i.split(" ") for i in input]
	camels = [Camel(cards, bid, CONV, True) for cards, bid in lines]

	camels.sort(key=lambda x: x.score, reverse=False)

	out = 0
	for i, c in enumerate(camels, start=1):
		out += c.bid * i
	return out

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
