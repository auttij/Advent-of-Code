import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from itertools import takewhile

@timer
@print_result
def part1(input):
	strs = input.split(",")

	out = 0
	for s in strs:
		temp = 0
		for c in s:
			temp += ord(c)
			temp = temp * 17
			temp = temp % 256
		out += temp
	return out

def hsh(s):
	temp = 0
	for c in s:
		temp += ord(c)
		temp = temp * 17
		temp = temp % 256
	return temp

@timer
@print_result
def part2(input):
	boxes = [[] for i in range(256)]

	strs = input.split(",")

	for s in strs:
		label = "".join(takewhile(lambda x: x.isalpha(), s))
		operator = s[len(label)]
		box = hsh(label)

		if operator == '-':
			for i, val in enumerate(boxes[box]):
				lbl, _ = val
				if label == lbl:
					del boxes[box][i]
			continue
		
		num = int(s[len(label) + 1:])
		added = False
		for i, val in enumerate(boxes[box]):
			lbl, _ = val
			if label == lbl:
				boxes[box][i] = (label, num)
				added = True
		if not added:
			boxes[box].append((label, num))
		
	out = 0
	for i, box in enumerate(boxes, start=1):
		for j, val in enumerate(box, start=1):
			lbl, lns = val
			out += i * j * lns
			
			# print(f"{lbl}: {i} * {j} * {lns}")
	return out


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
