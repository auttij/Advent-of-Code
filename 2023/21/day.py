import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from aocHelpers.helpers import adjacent

@timer
@print_result
def part1(input):
	for y, row in enumerate(input):
		for x, c in enumerate(row):
			if c == 'S':
				start = (y, x)

	stack = [start]
	for i in range(64):
		new_stack = set()
		while len(stack) > 0:
			top = stack.pop(0)
			adj = adjacent(top)
			for a in adj:
				if input[a[0]][a[1]] != '#':
					new_stack.add(a)
		stack = list(new_stack)
	return len(stack)

def fill(input, start, iter):
	out = []
	odd = set(start)
	even = set()
	stack = [start]
	prev = set()
	old = set()

	ly = len(input)

	i = 1
	while len(out) < 3:
		old = prev
		prev = set(stack)
		new_stack = set()

		while len(stack) > 0:
			top = stack.pop(0)
			adj = adjacent(top)
			for a in adj:
				y, x = a
				if input[y % len(input)][x % len(input[0])] != '#':
					new_stack.add(a)

		
		stack = list(new_stack.difference(old))
		if i % 2 == iter % 2:
			even = even.union(stack)

			if i % ly == iter % ly:
				out.append(len(even))
		else:
			odd = odd.union(stack)
			if i % ly == iter % ly:
				out.append(len(odd))
		
		i += 1

	return out


@timer
@print_result
def part2(input):
	for y, row in enumerate(input):
		for x, c in enumerate(row):
			if c == 'S':
				start = (y, x)

	goal = 26_501_365

	def f(n):
		a0, a1, a2 = fill(input, start, goal)

		b0 = a0
		b1 = a1-a0
		b2 = a2-a1
		return b0 + b1*n + (n*(n-1)//2)*(b2-b1)
	return f(goal//131)

def main(args=None):
	input = init(path.dirname(__file__), inputs.read_to_str_arr, args)
	if isinstance(input, str):
		# part1(input)
		part2(input)
	else:
		# part1(input.copy())
		part2(input.copy())

if __name__ == "__main__":
	main(argv[1:])
