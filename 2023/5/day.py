import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from itertools import repeat

@timer
@print_result
def part1(input):
	sections = [i.split('\n') for i in input.split("\n\n")]
	sections[0] = sections[0][0].split(": ")
	sections = [i[1:] for i in sections]

	seeds = [list(zip(list(map(int, i.split())), repeat(0))) for i in sections[0]][0]

	for section in sections[1:]:
		new_map = set()
		lines = [list(map(int, i.split())) for i in section]
		for src, rng in seeds:
			for i in range(src, src + rng + 1):
				found = False
				for dest, src2, rng2 in lines:
					if src2 < i and src2 + rng2 > i:
						j = i - src2
						new_map.add((dest + j, 0))
						found = True
							
				if not found:
					new_map.add((i, 0))

		seeds = sorted(list(new_map))
	return seeds[0][0]

class Function:
	def __init__(self, lines):
		self.tuples: list[tuple[int,int,int]] = [[int(x) for x in line.split()] for line in lines]

	def apply_one(self, x: int) -> int:
		for (dst, src, rng) in self.tuples:
			if src <= x < src + rng:
				return x + dst - src
		return x

	def apply_range(self, R: list[int, int]):
		A = []
		for (dest, src, rng) in self.tuples:
			src_end = src + rng
			NR = []
			while R:
				(st,ed) = R.pop()
				
				before = (st,min(ed,src))
				inter = (max(st, src), min(src_end, ed))
				after = (max(src_end, st), ed)
				if before[1]>before[0]:
					NR.append(before)
				if inter[1]>inter[0]:
					A.append((inter[0]-src+dest, inter[1]-src+dest))
				if after[1]>after[0]:
					NR.append(after)
			R = NR
		return A+R	

@timer
@print_result
def part2(input):
	sections = [i.split('\n') for i in input.split("\n\n")]
	sections[0] = sections[0][0].split(": ")
	sections = [i[1:] for i in sections]

	seeds = [list(map(int, i.split())) for i in sections[0]][0]
	pairs = [(val, seeds[2*i + 1]) for i, val in enumerate(seeds[::2])]
	out = []

	Fs = [Function(s) for s in sections[1:]]
	for st, sz in pairs:
		R = [(st, st+sz)]
		for f in Fs:
			R = f.apply_range(R)
		out.append(min(R)[0])
	return(min(out))

def main(args=None):
	input = init(path.dirname(__file__), inputs.read_to_str, args)
	if isinstance(input, str):
		part1(input)
		part2(input)
	else:
		part1(input.copy())
		part2(input.copy())

if __name__ == "__main__":
	main(argv[1:])
